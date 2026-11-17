"""
WHY:
The Ingredient model defines the structure and validation rules for ingredient
data used throughout the API. By centralizing these fields in a Pydantic model,
the application ensures that all ingredient-related input is strongly typed,
validated, and documented automatically in the OpenAPI schema. This improves
data consistency across endpoints and prevents malformed or incomplete ingredient
objects from entering the system.

DESIGN:
1. Inherit from BaseModel to leverage Pydantic's automatic validation, type
   enforcement, and serialization.
2. Require the fields specified by the project requirements:
   - name
   - category
3. Keep quantity optional as additional metadata that may be useful but is not
   required by the assignment specification.
4. Include an id field for consistency with recipe resources and future
   scalability.
5. Use Field() validation to prevent empty strings and enforce reasonable field
   lengths.
6. Keep the model simple and reusable across creation, retrieval, listing, and
   nested recipe operations.
7. Rely on FastAPI and Pydantic's automatic OpenAPI generation so ingredient
   structures appear clearly in Swagger UI.

Overall, this schema provides a validated and extensible representation of
ingredient data while remaining aligned with the project requirements.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Ingredient(BaseModel):
    """
    Core ingredient schema.
    """

    id: int | None = None

    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    category: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    quantity: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    model_config = ConfigDict(
        from_attributes=True
    )

