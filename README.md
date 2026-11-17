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