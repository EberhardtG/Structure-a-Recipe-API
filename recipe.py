"""
WHY:
The recipes router implements the core functionality required by the assignment:
    • GET /recipes — List all recipes
    • GET /recipes/{id} — Retrieve a specific recipe
    • POST /recipes — Create a new recipe

These endpoints form the foundation of a simple recipe management API. The router
also includes optional PUT and DELETE operations to demonstrate full CRUD behavior,
even though the assignment only requires creation and retrieval. Using an in‑memory
list keeps the implementation lightweight and focused on FastAPI routing concepts
rather than database integration.

DESIGN:
1. Use APIRouter with the prefix "/recipes" to keep recipe-related logic modular
   and separate from other resources such as ingredients.
2. Store recipes in an in‑memory list (recipes_db) to simulate persistent storage
   without introducing external dependencies. This makes the router easy to test
   and aligns with the educational goals of the assignment.
3. GET /recipes returns all stored recipes using response_model for automatic
   validation and clean OpenAPI documentation.
4. POST /recipes constructs a new RecipeResponse object, assigns a unique ID based
   on the current list length, and appends it to the in‑memory database. Returning
   the created recipe follows REST conventions and provides immediate feedback.
5. GET /recipes/{id} performs a simple lookup by integer ID and raises a 404 error
   when the recipe does not exist, ensuring predictable error handling.
6. PUT /recipes/{id} merges existing recipe data with any fields provided in the
   update payload. Using model_dump(exclude_unset=True) allows partial updates
   without requiring clients to resend unchanged fields.
7. DELETE /recipes/{id} removes the recipe from the list and returns a 204 No
   Content response, following REST best practices for delete operations.
8. All lookup-based endpoints use HTTPException to provide meaningful status codes
   and error messages, improving API usability and clarity.

This router is intentionally simple, readable, and aligned with FastAPI’s design
philosophy: strong typing, automatic documentation, modular routing, and clear,
predictable behavior.
"""




from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from app.schemas.recipes import RecipeCreate, RecipeResponse, RecipeUpdate

router = APIRouter(prefix="/recipes", tags=["recipes"])

recipes_db: list[RecipeResponse] = []


@router.get("/", response_model=list[RecipeResponse])
def list_recipes() -> list[RecipeResponse]:
    return recipes_db


@router.post("/", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: RecipeCreate) -> RecipeResponse:
    new_recipe = RecipeResponse(id=len(recipes_db) + 1, **recipe.model_dump())
    recipes_db.append(new_recipe)
    return new_recipe


@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int) -> RecipeResponse:
    for recipe in recipes_db:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")


@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe: RecipeUpdate) -> RecipeResponse:
    for index, existing_recipe in enumerate(recipes_db):
        if existing_recipe.id == recipe_id:
            updated_data = existing_recipe.model_dump()
            updated_data.update(recipe.model_dump(exclude_unset=True))
            recipes_db[index] = RecipeResponse(**updated_data)
            return recipes_db[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")


@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int) -> None:
    for index, recipe in enumerate(recipes_db):
        if recipe.id == recipe_id:
            del recipes_db[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
