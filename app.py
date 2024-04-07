from flask import Flask, jsonify, request, render_template
from bson import ObjectId
from bson.json_util import dumps 
from model import BookModel 

app = Flask(__name__)
book_model = BookModel() 

@app.route('/')
def status():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_book():
    book_data = request.get_json()
    if book_data:
        book_id = book_model.insert_book(book_data)
        if book_id:
            return jsonify({"message": "Book added successfully", "book_id": str(book_id)}), 201
        else:
            return jsonify({"message": "Error adding book"}), 500
    else:
        return jsonify({"message": "Error: No data provided"}), 400

@app.route('/books', methods=['GET'])
def get_books():
    books = book_model.get_all_books()
    return dumps(books), 200

@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book_id = ObjectId(book_id)
    except (TypeError, ValueError):
        return jsonify({"message": "Invalid book ID format"}), 400

    book = book_model.get_book_by_id(book_id)
    if book:
        return dumps(book), 200
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route('/update/<book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        book_id = ObjectId(book_id)
    except (TypeError, ValueError):
        return jsonify({"message": "Invalid book ID format"}), 400

    book_data = request.get_json()
    if book_data:
        updated = book_model.update_book(book_id, book_data)  
        if updated:
            return jsonify({"message": "Book updated successfully"}), 200
        else:
            return jsonify({"message": "Book not found"}), 404
    else:
        return jsonify({"message": "Error: No data provided"}), 400

@app.route('/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book_id = ObjectId(book_id)
    except (TypeError, ValueError):
        return jsonify({"message": "Invalid book ID format"}), 400

    deleted = book_model.delete_book(book_id)  
    if deleted:
        return jsonify({"message": "Book deleted successfully"}), 200
    else:
        return jsonify({"message": "Book not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)