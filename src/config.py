import os
import pydantic_settings
import pydantic


class AppConfig(pydantic_settings.BaseSettings):

    DB_URL: pydantic.PostgresDsn = os.environ.get(
        "DB_URL",
        "postgresql://auction:auction@localhost:5432/auction"
    )
    APP_HOST: str = os.environ.get("APP_HOST", "0.0.0.0")
    APP_PORT: int = os.environ.get("APP_PORT", 8000)
    UVICORN_WORKERS: int = os.environ.get("UVICORN_WORKERS", 1)
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")


app_config = AppConfig()