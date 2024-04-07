from pymongo import MongoClient
from flask import request
class BookModel:
    def __init__(self):
        try:
            self.client = MongoClient('mongodb+srv://feather158:Asif%40123@cluster0.efopvmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            # self.client = MongoClient('mongodb://localhost:27017/')
            self.db = self.client['Store']
            self.collection = self.db['Books']
            print("DB Connected")
        except Exception as e:
            print("Connection Error:", e)

    def insert_book(self, book_data):
        try:
            inserted_id = self.collection.insert_one(book_data).inserted_id
            return inserted_id
        except Exception as e:
            print("Error inserting book:", e)
            return None

    def get_all_books(self):
        try:
            books = list(self.collection.find())
            return books
        except Exception as e:
            print("Error getting all books:", e)
            return []

    def get_book_by_id(self, book_id):
        try:
            book = self.collection.find_one({"_id": book_id})
            return book
        except Exception as e:
            print("Error getting book by ID:", e)
            return None

    def update_book(self, book_id, book_data):
        try:
            res = self.collection.update_one({"_id": book_id}, {"$set": book_data})
            return res.modified_count > 0
        except Exception as e:
            print("Error updating book:", e)
            return False

    def delete_book(self, book_id):
        try:
            res = self.collection.delete_one({"_id": book_id})
            return res.deleted_count > 0
        except Exception as e:
            print("Error deleting book:", e)
            return False

if __name__ == "__main__":
    book_model = BookModel()
    book_data = request.get_json()

    inserted_id = book_model.insert_book(book_data)
    if inserted_id:
        print("Book inserted with ID:", inserted_id)

    all_books = book_model.get_all_books()
    print("All Books:", all_books)

    book_id = inserted_id
    book = book_model.get_book_by_id(book_id)
    print("Book by ID:", book)

    updated = book_model.update_book(book_id, {"genre": "Sci-Fi"})
    if updated:
        print("Book updated successfully")

    deleted = book_model.delete_book(book_id)
    if deleted:
        print("Book deleted successfully")
