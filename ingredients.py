"""
WHY:
The Ingredient model defines the structure and validation rules for ingredient
data used throughout the API. By centralizing these fields in a Pydantic model,
the application ensures that all ingredient-related input is strongly typed,
validated, and documented automatically in the OpenAPI schema. This improves
data consistency across endpoints and prevents malformed or incomplete ingredient
objects from entering the system.

DESIGN:
1. Inherit from BaseModel to leverage Pydantic’s automatic validation, type
   enforcement, and serialization. This keeps the model lightweight while
   providing robust input handling.
2. Use Field() to specify constraints such as min_length and max_length, ensuring
   that ingredient names and quantities meet basic formatting requirements and
   preventing empty or excessively long values.
3. Include a category field as an optional string to allow classification of
   ingredients (e.g., “dairy”, “produce”, “spice”) without requiring it for every
   entry. This provides flexibility while still supporting structured metadata.
4. Keep the model intentionally simple so it can be reused across multiple
   endpoints, including creation, listing, and lookup operations. The schema
   remains easy to understand and aligns with the educational goals of the
   assignment.
5. Rely on Pydantic’s automatic documentation generation so that the Ingredient
   model appears clearly in the API’s interactive docs, helping consumers know
   exactly what fields are expected.

Overall, this schema provides a clean, validated representation of ingredient
data that integrates seamlessly with FastAPI’s routing and documentation
features.
"""



from __future__ import annotations

from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    quantity: str = Field(..., min_length=1, max_length=100)
    category: str | None = Field(default=None, max_length=100)
