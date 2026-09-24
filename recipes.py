"""
WHY:
The recipe schema module defines all data models used to represent recipes across
the API. FastAPI relies heavily on Pydantic models for validation, serialization,
and automatic documentation, so having a clear and well‑structured set of recipe
schemas ensures consistent behavior across creation, retrieval, updating, and
database representation.

By separating base fields, creation fields, update fields, and response fields,
the API can enforce different validation rules depending on the operation. This
mirrors real‑world API design, where the data required to create a resource is
not always the same as the data returned to clients or stored internally.

DESIGN:
1. RecipeBase serves as the foundational schema containing all core recipe
   attributes. It defines validation rules (min_length, ge, max_length) and
   ensures that every recipe has a consistent structure. Optional fields such as
   description, cuisine, and cook_time_minutes allow flexibility while still
   enforcing strong typing.
2. The ingredients field uses a list of Ingredient models, demonstrating nested
   Pydantic validation and enabling structured recipe composition.
3. model_config = ConfigDict(from_attributes=True) allows the model to be
   constructed from ORM objects or attribute-based sources, improving compatibility
   with future database integrations.
4. RecipeCreate inherits from RecipeBase without modification, reflecting that
   creation requires the same fields as the base model. This keeps the API simple
   while maintaining clear semantic separation between “base definition” and
   “creation payload.”
5. RecipeUpdate defines all fields as optional and uses exclude_unset=True during
   updates. This enables partial updates, allowing clients to modify only the
   fields they care about without resending the entire recipe object.
6. RecipeInDB extends RecipeBase by adding an id field, representing how recipes
   are stored internally. This separates internal persistence concerns from
   external API concerns.
7. RecipeResponse inherits from RecipeInDB to define the structure returned to
   clients. This ensures that API responses always include the recipe’s id and
   all validated fields, providing a predictable and well‑documented output format.

Overall, this schema module provides a clean, layered design that supports strong
validation, clear separation of concerns, and scalable API behavior. It aligns
with FastAPI’s philosophy of explicit typing, modularity, and automatic
documentation.
"""



from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.ingredients import Ingredient


class RecipeBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    ingredients: list[Ingredient] = Field(default_factory=list)
    instructions: str = Field(..., min_length=1)
    cuisine: str | None = Field(default=None, max_length=100)
    prep_time_minutes: int | None = Field(default=None, ge=1)
    cook_time_minutes: int | None = Field(default=None, ge=1)
    servings: int | None = Field(default=None, ge=1)

    model_config = ConfigDict(from_attributes=True)


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    ingredients: list[Ingredient] | None = None
    instructions: str | None = Field(default=None, min_length=1)
    cuisine: str | None = Field(default=None, max_length=100)
    prep_time_minutes: int | None = Field(default=None, ge=1)
    cook_time_minutes: int | None = Field(default=None, ge=1)
    servings: int | None = Field(default=None, ge=1)


class RecipeInDB(RecipeBase):
    id: int


class RecipeResponse(RecipeInDB):
    pass
