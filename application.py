import os

from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    if session.get('username'):
        flash('Hi ' + session.get('username') + '! You can now search for books based on the: title, ISBN, or name of the author.')
    else:
        flash('Please login to search for books!')
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        with engine.connect() as connection:
            qry = text("select * from users where username=:u and password=:p ")
            users = connection.execute(qry, {"u": username, "p": password})
        if users.first():
            session["username"] = username
            return redirect(url_for('index'))
        else:
            flash('Username or Password is incorrect!')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session["username"] = None
    return redirect(url_for('index'))

@app.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Username and Password are required!')
        else:
            with engine.connect() as connection:
                qry = text("select * from users where username=:u")
                users = connection.execute(qry, {"u": username})
            if users.first():
                flash('That username already exists! Please choose another username.')
            else:
                with engine.connect() as connection:
                    qry = text("insert into users(username,password) values (:u, :p)")
                    connection.execute(qry, {"u": username, "p": password})
                    connection.commit()
                    connection.close()
                return redirect(url_for('index'))
        
    return render_template('register.html')

@app.route("/search")
def search():
    if not session.get('username'):
        return redirect(url_for('index'))

    qry = "select * from books"
    has_where = False
    if 'isbn' in request.args and request.args['isbn'] != '':
        qry = qry + " where isbn like '%" + request.args['isbn'] + "%'"
        has_where = True

    if 'title' in request.args and request.args['title'] != '':
        if has_where: 
            qry = qry + " and"
        else:
            qry = qry + " where"
        qry = qry + " title like '%" + request.args['title'] + "%'"
        has_where = True

    if 'author' in request.args and request.args['author'] != '':
        if has_where: 
            qry = qry + " and"
        else:
            qry = qry + " where"
        qry = qry + " author like '%" + request.args['author'] + "%'"
        has_where = True

    if not has_where:
        return render_template('search.html', books=[])

    with engine.connect() as connection:
        books = connection.execute(text(qry)).all()
    
    if not books:
        flash('No matching books found!')

    return render_template('search.html', books=books)

@app.route("/book/<string:isbn>")
def book(isbn):
    if not session.get('username'):
        return redirect(url_for('index'))
    
    with engine.connect() as connection:
        qry = text("select * from books where isbn=:isbn")
        books = connection.execute(qry, {"isbn": isbn})
        qry = text("select * from reviews where isbn=:isbn")
        reviews = connection.execute(qry, {"isbn": isbn})

    return render_template('book.html', book=books.first(), reviews=reviews)

@app.route("/review", methods=["POST"])
def review():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    
    isbn = request.form['isbn']
    comment = request.form['comment']
    if not comment:
        flash('Please input your comment!')
    else:
        with engine.connect() as connection:
            qry = text("insert into reviews(isbn,username,comment) values (:isbn, :username, :comment)")
            connection.execute(qry, {"isbn": isbn, "username": username, "comment": comment})
            connection.commit()
            connection.close()
    return redirect(url_for('book', isbn=isbn))