# ENGO551/651 - Lab 2 Assignment
The objective of this lab was to become more comfortable with writing code in Python, gain experience with Flask, intereact with databases through the use of SQL, and learn to interact with APIs. 

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
- application.py : the Python script containing all the functionality for logging in, searching for books, etc. Update: now utilizes Gemini and Google Books API. 
- import.py : the Python script that connects to the database and loads data in
- books.csv : a CSV file that contains all the book data
- schema.sql : the SQL file used for setting the structure of the database 
- run.bat : a batch file used to run the application.py script and pass the database URL

## Requirements Met
1. All requirements from Lab 1 are met. 
2. Users are now able to leave a rating from 1 to 5, while still being able to write a review. Additionally a user may only leave one review. 
3. From the Google Books API, the average rating and number of ratings is shown for each book on the webpage.  
4. On the book webpage, the full description as well as the summarized description from Gemini API. 
5. Users can make a GET request to the website's /api/<isbn> route, in which a JSON response is returned including the book's title author, published date, ISBN (both ISBN_10 and ISBN_13 types), review count (number of ratings), average rating, description (Book API response), and summarized description (Gemini response).
6. Null values are returned when the API doesn't have values for fields, and if an ISBN requested is not found in the database, a 404 error is returned. 
7. Raw SQLAlchemy queries are used. 


## Additional Details about the Lab Assignment 
To run the book review website please follow the steps below: 
1. Set up your environment with all the necessary dependencies.
2. Run the import.py Python script to load all the book data into the database (project1)
3. Run the run.bat file in a command terminal (this runs the application.py file and passes the database URL). Update: the Gemini API key is not included in this file, as it is private. 
4. Explore the website, which now utlizes API! :D
