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

if __name__ == "__main__":
    app.run(debug=True)