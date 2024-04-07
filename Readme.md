# Online Book Store API using MongoDB and Flask

This is a Flask-based RESTful API for managing books. It allows users to perform CRUD (Create, Read, Update, Delete) operations on a collection of books stored in a MongoDB. The python-MongoDB connector is PyMongo.

## Live Link

[Click here to explore](https://flask-nmc0.onrender.com/)

## Endpoints

#### Add a Book

- **URL:** `/add`
- **Method:** `POST`
- **Request Body:**

```
{
    "title": "Sample Book",
    "author": "ABCD",
    "isbn": "123456678",
    "year": 2024,
    "genre": "Romance",
    "publisher": "ABC",
    "language": "Hindi",
    "pages": 123,
    "description": "Sample Description",
    "price": "₹899"
}
```

- **Response:**

```
{
    "book_id": "66122aba32ac09f66427bb32",
    "message": "Book added successfully"
}
```

#### Get All Books

- **URL:** `/books`
- **Method:** `GET`
- **Response:** JSON array containing details of all books.

#### Get a Book by ID

- **URL:** `/books/<book_id>`
- **Method:** `GET`
- **Response:** JSON object containing details of the requested book.

#### Update a Book

- **URL:** `/update/<book_id>`
- **Method:** `PUT`
- **Request Body:**

```
{
    "title": "Updated Book",
    "author": "ABCDE",
    "isbn": "1234566789",
    "year": 2023,
    "genre": "Drama",
    "publisher": "ABCD",
    "language": "English",
    "pages": 23,
    "description": "Updated Description",
    "price": "₹99"
}
```

- **Response:**

```
{
    "message": "Book updated successfully"
}
```

#### Delete a Book

- **URL:** `/delete/<book_id>`
- **Method:** `DELETE`
- **Response:**

```
{
    "message": "Book deleted successfully"
}
```

## Installation

### Requirements

- Python 3.x
- MongoDB
- Flask
- pymongo

First, you should [install MongoDB](https://docs.mongodb.com/manual/installation/)

then install all dependencies by running the following command:

```
pip install -r requirements.txt
```

It will install Flask and PyMongo.

- **Windows**:
  Start MongoDB as a service or manually.

- **macOS**:
  Start MongoDB using appropriate commands for your system.
- **Linux**: Run the program as follows

To run the program, first you should make sure MongoDB is running, start it using:

```
sudo systemctl start mongod
```

then, run the program:

```
python app.py
```

Open your browser and go to `localhost:5000	` .
