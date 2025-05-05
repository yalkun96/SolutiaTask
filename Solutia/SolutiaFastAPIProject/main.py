from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os
app = FastAPI()

BOOKS_FILE = "books.json"

class Book(BaseModel):
    title: str
    price: float



def load_books() -> List[dict]:
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as f:
            json.dump([], f)
        return []
    with open(BOOKS_FILE, "r") as f:
        return json.load(f)

def save_books(books: List[dict]):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

@app.post("/books/", response_model=Book, status_code=201)
def create_book(book: Book):
    books = load_books()
    # Проверка на дублирование по названию
    if any(b["title"] == book.title for b in books):
        raise HTTPException(status_code=400, detail="Book with this title already exists")
    books.append(book.dict())
    save_books(books)
    return book


@app.get("/books/", response_model=List[Book])
def get_books():
    return load_books()

@app.get("/books/{title}", response_model=Book)
def get_book(title: str):
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{title}", response_model=Book)
def update_book(title: str, updated_book: Book):
    books = load_books()
    for idx, book in enumerate(books):
        if book["title"].lower() == title.lower():
            books[idx] = updated_book.dict()
            save_books(books)
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{title}", status_code=204)
def delete_book(title: str):
    books = load_books()
    new_books = [book for book in books if book["title"].lower() != title.lower()]
    if len(books) == len(new_books):
        raise HTTPException(status_code=404, detail="Book not found")
    save_books(new_books)
    return None
