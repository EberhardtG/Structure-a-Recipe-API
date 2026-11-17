"""
WHY:
The Settings class centralizes application configuration in a single, typed,
validated location. FastAPI projects often rely on environment variables for
runtime configuration such as database URLs, debug flags, and application
metadata. Using Pydantic Settings provides a structured and reliable way to load
these values while ensuring they conform to expected types.

This approach keeps configuration separate from business logic and makes the
application easier to deploy across different environments including
development, testing, and production.

DESIGN:
1. Inherit from BaseSettings to automatically load values from environment
   variables and .env files.
2. Define strongly typed fields so configuration values are validated at
   application startup.
3. Use SettingsConfigDict for Pydantic v2 compliant configuration management.
4. Provide sensible defaults so the application can run immediately during
   development.
5. Create a single shared Settings instance that can be imported throughout
   the application.
6. Use a centralized settings object so FastAPI metadata, database settings,
   and environment configuration remain consistent across modules.

Overall, this module provides a scalable and maintainable approach to
configuration management that aligns with FastAPI and Pydantic v2 best
practices.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    and/or a .env file.
    """

    app_name: str = "Recipes & Ingredients API"
    app_version: str = "1.0.0"
    app_description: str = (
        "A modular FastAPI application for managing recipes and ingredients."
    )

    debug: bool = False

    database_url: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()