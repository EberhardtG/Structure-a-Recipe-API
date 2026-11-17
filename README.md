# 🍽️ FastAPI Recipes & Ingredients API

A modular FastAPI application that manages Recipes and Ingredients using separate routers, schema modules, and centralized configuration.

This project demonstrates:

- FastAPI router organization
- Pydantic schema validation
- Environment-based configuration using pydantic-settings
- In-memory data persistence
- CRUD operations
- Proper HTTP status codes
- Scalable project structure

---

# 📁 Project Structure

```text
my-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── recipes.py
│   │   └── ingredients.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── recipes_router.py
│       └── ingredients_router.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# 🧠 Overview

The API exposes two resource groups:

## Recipes (`/recipes`)

Supported operations:

| Method | Endpoint | Description |
|----------|------------|------------|
| GET | `/recipes` | List all recipes |
| GET | `/recipes/{id}` | Get recipe by ID |
| POST | `/recipes` | Create recipe |
| PUT | `/recipes/{id}` | Update recipe |
| DELETE | `/recipes/{id}` | Delete recipe |

---

## Ingredients (`/ingredients`)

Supported operations:

| Method | Endpoint | Description |
|----------|------------|------------|
| GET | `/ingredients` | List all ingredients |
| POST | `/ingredients` | Create ingredient |
| GET | `/ingredients/{name}` | Get ingredient by name |
| DELETE | `/ingredients/{name}` | Delete ingredient |

---

# 🧩 Data Models

## Ingredient Schema

Located in:

```text
app/schemas/ingredients.py
```

Required fields:

```python
name: str
category: str
```

Optional fields:

```python
id: int
quantity: str
```

Example:

```json
{
  "id": 1,
  "name": "Tomato",
  "category": "Produce",
  "quantity": "2 cups"
}
```

---

## Recipe Schemas

Located in:

```text
app/schemas/recipes.py
```

### Required Fields

```python
title
cuisine
prep_time_minutes
servings
```

### Optional Fields

```python
description
ingredients
instructions
cook_time_minutes
```

---

### Schema Layers

#### RecipeBase

Defines common recipe attributes and validation rules.

#### RecipeCreate

Used when creating recipes.

#### RecipeUpdate

Used for partial updates.

Supports:

```python
exclude_unset=True
```

so clients only need to send modified fields.

#### RecipeInDB

Adds:

```python
id
```

for persistence.

#### RecipeResponse

Returned to API consumers.

---

# 🔌 Router Design

## Recipes Router

Located in:

```text
app/routers/recipes_router.py
```

Features:

- In-memory recipe storage
- Auto-incrementing IDs
- CRUD operations
- 404 handling
- 201 Created responses
- 204 No Content deletes

Example:

```python
next_recipe_id = 1
```

Used instead of:

```python
len(recipes_db) + 1
```

to prevent duplicate IDs after deletions.

---

## Ingredients Router

Located in:

```text
app/routers/ingredients_router.py
```

Features:

- In-memory ingredient storage
- Name lookup
- Create/list/delete operations
- Consistent HTTP responses

---

# ⚙️ Configuration

Located in:

```text
app/config.py
```

Uses:

```python
pydantic-settings
```

to load configuration from:

```text
.env
```

Available settings:

```python
app_name
app_description
app_version
debug
database_url
```

Configuration is loaded through a shared:

```python
settings = Settings()
```

instance.

---

# 🚀 Running the Application

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

Expected output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# 📖 Swagger Documentation

Once the server is running, open:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger should display two sections:

```text
recipes
ingredients
```

with all endpoints grouped under their respective router tags.

---

# 🧪 Sample Recipe Payload

```json
{
  "title": "Chicken Alfredo",
  "cuisine": "Italian",
  "prep_time_minutes": 20,
  "servings": 4,
  "description": "Creamy pasta dish",
  "ingredients": [
    {
      "name": "Chicken Breast",
      "category": "Protein",
      "quantity": "2"
    }
  ],
  "instructions": "Cook chicken and combine with pasta.",
  "cook_time_minutes": 25
}
```

---

# 📌 Design Philosophy

This project follows a modular API architecture:

- Schemas handle validation
- Routers handle HTTP logic
- Configuration is centralized
- Models are reusable
- Endpoints return consistent responses
- Business logic remains separated from application startup

This structure closely mirrors real-world FastAPI projects and provides a foundation for future database integration.

---

# 📈 Future Enhancements

Potential improvements include:

- SQLAlchemy integration
- SQLite or PostgreSQL database
- JWT Authentication
- Pagination
- Search and filtering
- Unit testing with pytest
- Docker support
- Deployment to Render or Azure

---

# 📄 License

This project was created for educational purposes while learning FastAPI, API design, schema validation, and application architecture.

# **FastAPI Recipes & Ingredients API**

A modular FastAPI application implementing two resources—**Recipes** and **Ingredients**—each with their own Pydantic schemas, routers, and in‑memory persistence. This project demonstrates clean API design, strong validation, environment‑based configuration, and a scalable application structure suitable for learning or prototyping.

---

## **📁 Project Structure**

```
my-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── schemas/
│   │   ├── ingredients.py
│   │   └── recipes.py
│   │
│   └── routers/
│       ├── ingredients_router.py
│       └── recipes_router.py
│
├── .env
└── README.md
```

---

## **🧠 Overview**

This API exposes two main resources:

### **Recipes (`/recipes`)**
Implements:
- GET `/recipes` — List all recipes  
- GET `/recipes/{id}` — Retrieve a specific recipe  
- POST `/recipes` — Create a new recipe  
- PUT `/recipes/{id}` — Update a recipe *(extra)*  
- DELETE `/recipes/{id}` — Delete a recipe *(extra)*  

Backed by:
- `RecipeBase`
- `RecipeCreate`
- `RecipeUpdate`
- `RecipeInDB`
- `RecipeResponse`

### **Ingredients (`/ingredients`)**
Implements:
- GET `/ingredients` — List all ingredients  
- POST `/ingredients` — Create an ingredient  
- GET `/ingredients/{name}` — Retrieve ingredient by name *(extra)*  
- DELETE `/ingredients/{name}` — Delete ingredient *(extra)*  

Backed by:
- `Ingredient`

---

## **🧩 Schemas**

### **Ingredient Schema**  
Located in `schemas/ingredients.py`

Defines:
- `name` — required  
- `quantity` — required  
- `category` — optional  

Used for:
- Ingredient creation  
- Ingredient listing  
- Nested inside recipe schemas  

---

### **Recipe Schemas**  
Located in `schemas/recipes.py`

Includes:

#### **RecipeBase**
Core recipe fields:
- `title`
- `description`
- `ingredients` (list of `Ingredient`)
- `instructions`
- `cuisine`
- `prep_time_minutes`
- `cook_time_minutes`
- `servings`

#### **RecipeCreate**
Inherits from `RecipeBase`  
Used for POST requests.

#### **RecipeUpdate**
All fields optional  
Used for partial updates.

#### **RecipeInDB**
Extends `RecipeBase` with:
- `id`

Represents stored recipes.

#### **RecipeResponse**
Extends `RecipeInDB`  
Used for API responses.

---

## **🔌 Routers**

### **Recipes Router**  
Located in `routers/recipes_router.py`

Implements:
- In‑memory list `recipes_db`
- Full CRUD operations
- ID‑based lookup
- Partial updates using `exclude_unset=True`
- Proper HTTP status codes (201, 404, 204)

### **Ingredients Router**  
Located in `routers/ingredients_router.py`

Implements:
- In‑memory list `ingredients_db`
- Case‑insensitive name lookup
- Simple create/list/delete operations
- Proper HTTP status codes (201, 404, 204)

---

## **⚙ Configuration (config.py)**

Located in `config.py`

Uses `pydantic-settings` to load:
- `app_name`
- `debug`
- `database_url`

Supports `.env` file loading with:
- UTF‑8 encoding  
- Case‑insensitive environment variables  

Provides a single `settings` instance for global configuration.

---

## **🚀 Running the Application**

### **Install dependencies**
```
pip install fastapi uvicorn pydantic-settings
```

### **Start the server**
```
uvicorn app.main:app --reload
```

### **Open API documentation**
Swagger UI:
```
http://127.0.0.1:8000/docs
```

ReDoc:
```
http://127.0.0.1:8000/redoc
```

---

## **📌 Design Philosophy**

This project follows a modular FastAPI architecture:

- **Schemas** define strict data validation and structure  
- **Routers** encapsulate resource‑specific logic  
- **main.py** integrates all routers into a single application  
- **config.py** centralizes configuration  
- **In‑memory lists** simulate persistence without external dependencies  

This structure mirrors real-world FastAPI applications while remaining simple enough for instructional use.

---

## **📈 Possible Enhancements**

- Replace in‑memory lists with SQLite + SQLAlchemy  
- Add authentication (JWT)  
- Add search/filter endpoints  
- Add pagination  
- Add unit tests with pytest  
