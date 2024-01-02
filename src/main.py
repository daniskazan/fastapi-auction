import fastapi
import uvicorn

from api.routing import router

from core.common.models.base import BaseORMModel
from core.common.session import engine

from config import app_config


app = fastapi.FastAPI()

app.include_router(router)


if __name__ == "__main__":
    BaseORMModel.metadata.create_all(bind=engine)
    uvicorn.run(
        app="main:app",
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        workers=app_config.UVICORN_WORKERS,
    )