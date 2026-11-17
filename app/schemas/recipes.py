"""
WHY:
The recipe schema module defines all data models used to represent recipes across
the API. FastAPI relies heavily on Pydantic models for validation, serialization,
and automatic documentation, so having a clear and well-structured set of recipe
schemas ensures consistent behavior across creation, retrieval, updating, and
database representation.

By separating base fields, creation fields, update fields, and response fields,
the API can enforce different validation rules depending on the operation. This
mirrors real-world API design, where the data required to create a resource is
not always the same as the data returned to clients or stored internally.

DESIGN:
1. RecipeBase serves as the foundational schema containing all core recipe
   attributes and validation rules.
2. Required fields match the project specification:
   - title
   - cuisine
   - prep_time_minutes
   - servings
3. Ingredients use nested Ingredient models to demonstrate structured
   validation and composition.
4. RecipeCreate inherits directly from RecipeBase and is used for creation.
5. RecipeUpdate makes every field optional so partial updates can be performed
   using model_dump(exclude_unset=True).
6. RecipeInDB extends RecipeBase with an id field for persistence.
7. RecipeResponse extends RecipeInDB and defines the format returned to clients.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.ingredients import Ingredient


class RecipeBase(BaseModel):
    """
    Core recipe fields shared across create, update,
    database, and response models.
    """

    # Required by assignment specification
    title: str = Field(
        ...,
        min_length=1,
        max_length=200
    )

    cuisine: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    prep_time_minutes: int = Field(
        ...,
        ge=1
    )

    servings: int = Field(
        ...,
        ge=1
    )

    # Optional enhancements
    description: str | None = None

    ingredients: list[Ingredient] = Field(
        default_factory=list
    )

    instructions: str | None = Field(
        default=None,
        min_length=1
    )

    cook_time_minutes: int | None = Field(
        default=None,
        ge=1
    )

    model_config = ConfigDict(
        from_attributes=True
    )


class RecipeCreate(RecipeBase):
    """
    Schema used when creating recipes.
    """
    pass


class RecipeUpdate(BaseModel):
    """
    Schema used for partial recipe updates.
    Every field is optional to support PATCH/PUT
    operations with exclude_unset=True.
    """

    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=200
    )

    cuisine: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    prep_time_minutes: int | None = Field(
        default=None,
        ge=1
    )

    servings: int | None = Field(
        default=None,
        ge=1
    )

    description: str | None = None

    ingredients: list[Ingredient] | None = None

    instructions: str | None = Field(
        default=None,
        min_length=1
    )

    cook_time_minutes: int | None = Field(
        default=None,
        ge=1
    )


class RecipeInDB(RecipeBase):
    """
    Internal database representation.
    """

    id: int


class RecipeResponse(RecipeInDB):
    """
    API response model.
    """
    pass