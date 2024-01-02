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


app_config = AppConfig()