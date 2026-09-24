"""
WHY:
The ingredients router provides a simple, self‑contained resource for managing
ingredient data within the API. The assignment requires two endpoints:
    • GET /ingredients — List all ingredients
    • POST /ingredients — Create a new ingredient

This router fulfills those requirements while also adding two optional but useful
endpoints (GET by name and DELETE by name) to demonstrate full CRUD-style
interactions. Using an in‑memory list keeps the implementation lightweight and
focused on FastAPI routing concepts rather than persistence.

DESIGN:
1. Use APIRouter with the prefix "/ingredients" to keep the resource modular and
   allow clean separation from other API components such as recipes.
2. Store ingredients in an in‑memory list (ingredients_db) to simulate a simple
   database. This keeps the project easy to test without external dependencies.
3. GET /ingredients returns the entire list, using response_model for automatic
   validation and documentation.
4. POST /ingredients accepts an Ingredient schema instance and appends it to the
   in‑memory database. Returning the created ingredient provides immediate feedback
   to the client and aligns with REST conventions.
5. GET /ingredients/{ingredient_name} performs a case‑insensitive lookup to make
   the endpoint more user-friendly and avoid strict matching issues.
6. DELETE /ingredients/{ingredient_name} removes the ingredient from the list and
   returns a 204 No Content status, following REST best practices for delete
   operations.
7. All lookup-based endpoints raise HTTP 404 when an ingredient is not found,
   ensuring predictable and meaningful error responses.

This router is intentionally simple, readable, and aligned with FastAPI’s design
philosophy: clear routing, strong typing, automatic documentation, and predictable
behavior.
"""



from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.recipes import Ingredient

router = APIRouter(prefix="/ingredients", tags=["ingredients"])

ingredients_db: list[Ingredient] = []


@router.get("/", response_model=list[Ingredient])
def list_ingredients() -> list[Ingredient]:
    return ingredients_db


@router.post("/", response_model=Ingredient, status_code=status.HTTP_201_CREATED)
def create_ingredient(ingredient: Ingredient) -> Ingredient:
    ingredients_db.append(ingredient)
    return ingredient


@router.get("/{ingredient_name}", response_model=Ingredient)
def get_ingredient(ingredient_name: str) -> Ingredient:
    for ingredient in ingredients_db:
        if ingredient.name.lower() == ingredient_name.lower():
            return ingredient
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")


@router.delete("/{ingredient_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient(ingredient_name: str) -> None:
    for index, ingredient in enumerate(ingredients_db):
        if ingredient.name.lower() == ingredient_name.lower():
            del ingredients_db[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
