from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Book Management API")

# TODO: Define your Book model here using Pydantic BaseModel
# Include fields: id, title, author, publication_year, genre

# TODO: Create an in-memory storage (list or dict) for books

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Book Management API"}

# TODO: Implement POST /books endpoint to create a new book

# TODO: Implement GET /books endpoint to retrieve all books

# TODO: Implement GET /books/{book_id} endpoint to retrieve a specific book

# TODO: Implement PUT /books/{book_id} endpoint to update a book

# TODO: Implement DELETE /books/{book_id} endpoint to delete a book

# TODO: Implement GET /books/search endpoint with query parameters for filtering

# Run with: uvicorn starter-code:app --reload
