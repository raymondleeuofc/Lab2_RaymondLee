import psycopg2
import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = []
        for row in csv_reader:
            data.append(row)
    
    return data

conn = psycopg2.connect(database="project1",
                        host="localhost",
                        port="5432",
                        user="postgres",
                        password="postShark7")
cur = conn.cursor()

# create schema
with open('schema.sql', 'r') as f:
    cur.execute(f.read())
        
# read and insert rows
csv_rows = read_csv('books.csv')
for row in csv_rows:
    cur.execute("""
    INSERT INTO books(isbn,title,author,year)
    VALUES (%s, %s, %s, %s);
    """,
    row)

conn.commit()
conn.close()
