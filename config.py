"""
WHY:
The Settings class centralizes application configuration in a single, typed,
validated location. FastAPI projects often rely on environment variables for
runtime configuration—such as database URLs, debug flags, and application
metadata. Using Pydantic Settings provides a structured, reliable way to load
these values while ensuring they conform to expected types. This approach keeps
configuration separate from business logic and makes the application easier to
deploy across different environments (development, testing, production).

DESIGN:
1. Inherit from BaseSettings to automatically load values from environment
   variables, .env files, or system-level configuration. This ensures the
   application can be configured without modifying code.
2. Define strongly typed fields (app_name, debug, database_url) so that invalid
   configuration values are caught early, improving reliability and reducing
   runtime errors.
3. Use SettingsConfigDict and the inner Config class to specify .env behavior,
   encoding, and case sensitivity. These settings ensure consistent loading of
   environment variables regardless of deployment environment.
4. Provide default values for all fields so the application can run even when
   no external configuration is supplied. This simplifies development and makes
   the API immediately usable.
5. Instantiate a single Settings() object at module level so configuration is
   loaded once and shared across the application. This avoids repeated parsing
   and ensures consistent configuration access.

Overall, this settings module provides a clean, scalable foundation for managing
application configuration using Pydantic’s robust validation and FastAPI’s
environment-driven design philosophy.
"""




from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "my recipes"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()
