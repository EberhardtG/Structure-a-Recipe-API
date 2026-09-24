"""
WHY:
The main application file serves as the central entry point for the FastAPI
project. Its purpose is to initialize the FastAPI instance, configure global
application metadata, and register all routers that define the API’s resources.
By keeping main.py focused on application setup rather than business logic, the
project remains modular, readable, and easy to extend.

This file also acts as the integration layer between independent routers such as
recipes and ingredients. Each router encapsulates its own endpoints and logic,
and main.py brings them together into a single cohesive API. This separation of
concerns mirrors real-world FastAPI project structure and supports scalability as
additional resources or features are added.

DESIGN:
1. Create a FastAPI application instance with metadata (title, description,
   version) to provide clear documentation in the automatically generated Swagger
   UI. This improves API discoverability and helps consumers understand the
   purpose of the service.
2. Import routers from their respective modules and register them using
   app.include_router(). This modular design keeps resource logic isolated and
   prevents main.py from becoming cluttered with endpoint definitions.
3. Use descriptive tags and prefixes within each router so that the OpenAPI
   documentation groups endpoints logically (e.g., “recipes” and “ingredients”).
4. Avoid storing business logic or data structures in main.py. Instead, rely on
   routers and schemas to define behavior and validation. This keeps main.py
   lightweight and focused solely on application configuration.
5. Maintain a clear and predictable application startup path so that running the
   server (via uvicorn) consistently loads all registered routes and exposes the
   full API.

Overall, main.py acts as the orchestrator of the FastAPI application—clean,
minimal, and designed to scale as the project grows.
"""



from fastapi import FastAPI

from app.routes.ingredients_routes import router as ingredients_router
from app.routes.recipe import router as recipe_router

# Create the application instance - this is your API
app = FastAPI(
    title="My Recipes",
    description="A simple API for managing recipes",
    version="1.0.0"
)

app.include_router(recipe_router)
app.include_router(ingredients_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to My Recipes"}
