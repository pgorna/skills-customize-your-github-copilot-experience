# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, fast REST APIs using the FastAPI framework in Python. You'll create a complete API with CRUD operations, data validation, and automatic documentation.

## 📝 Tasks

### 🛠️	Create a Book Management API

#### Description
Build a REST API for managing a collection of books. The API should support creating, reading, updating, and deleting book records with proper data validation and response handling.

#### Requirements
Completed API should:

- Include a `Book` model with fields: id, title, author, publication_year, and genre
- Implement POST endpoint to add new books with automatic validation
- Implement GET endpoint to retrieve all books or a specific book by ID
- Implement PUT endpoint to update existing book information
- Implement DELETE endpoint to remove books from the collection
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Store data in memory using a Python list or dictionary


### 🛠️	Add Search and Filter Functionality

#### Description
Enhance your API with search capabilities to allow users to find books based on different criteria.

#### Requirements
Completed program should:

- Implement GET endpoint with query parameters for filtering by author
- Add query parameter for filtering by genre
- Add query parameter for filtering by publication year range
- Return empty list with 200 status when no books match the criteria
- Support combining multiple filter parameters in a single request
