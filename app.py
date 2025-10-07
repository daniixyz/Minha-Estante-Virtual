from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.get("/")
def index():
    books = []
    with open('books.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            books.append(row)

    return render_template("index.html", books=books)

@app.get("/book/<int:book_id>")
def book_details(book_id):
    found_book = None

    with open('books.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for book in csv_reader:
            if int(book['id']) == book_id:
                found_book = book
                break
    
    if found_book:
        return render_template("details.html", book=found_book)

    else:
        return "Book not found!", 404


if __name__ == "__main__":
    app.run(debug=True)