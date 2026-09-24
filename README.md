
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
