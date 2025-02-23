# ENGO551/651 - Lab 1 Assignment
The objective of this lab was to become more comfortable with writing code in Python, gain experience with Flask, and to intereact with databases through the use of SQL. 

## Important Folders and Files
- static : contains the style sheets
    - styles.css : CSS style sheet file
    - styles.scss : SCSS style sheet file
- templates : contains the html files used on the website
    - base.html : the base webpage format that all other html files inherit
    - book.html : the webpage file for a specific book 
    - index.html : the main webpage file
    - login.html : the login webpage file
    - register.html : the registration webpage file
    - search.html : the search webpage file
- application.py : the Python script containing all the functionality for logging in, searching for books, etc
- import.py : the Python script that connects to the database and loads data in
- books.csv : a CSV file that contains all the book data
- schema.sql : the SQL file used for setting the structure of the database 
- run.bat : a batch file used to run the application.py script and pass the database URL

## Requirements Met
1. The user is able to register as a user, log in and log out of the website with a valid username and password. 
2. With the import.py script, the data from books.csv is loaded into a local database which was created using the schema.sql file. 
3. The user is able to search by either whole: titles, ISBN, or the name of the author (or by a partial match). Afterwards, all results are provided that match the entry, and in the case of no matches, the website states that no books were found. 
4. After finding a book, the user can click on the ISBN of the book which directs them to a webpage of the book which includes the: ISBN, title, author name, and publication year. In the webpage, the user can choose to leave a review of the book which is then stored in the reviews table in the dtabase. 
5. Only raw SQL queries were used for this book review website, with all queries found in the application.py script. 


## Additional Details about the Lab Assignment 
To run the book review website please follow the steps below: 
1. Set up your environment with all the necessary dependencies.
2. Run the import.py Python script to load all the book data into the database (project1)
3. Run the run.bat file in a command terminal (this runs the application.py file and passes the database URL)
4. Explore the website! :D
