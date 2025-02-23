DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    isbn CHAR(10) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year CHAR(4) NOT NULL
);

CREATE TABLE users (
    username VARCHAR(16) PRIMARY KEY,
    password VARCHAR(16) NOT NULL
);

CREATE TABLE reviews (
    id SERIAL,
    isbn CHAR(10) NOT NULL,
    username VARCHAR(16) NOT NULL,
    comment VARCHAR(255) NOT NULL,
    CONSTRAINT fk_book
      FOREIGN KEY(isbn)
        REFERENCES books(isbn),
    CONSTRAINT fk_user
      FOREIGN KEY(username)
        REFERENCES users(username)
);