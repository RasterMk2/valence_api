import fastapi
from tortoise.contrib.fastapi import register_tortoise


def register(app: fastapi.FastAPI) -> None:
    register_tortoise(
        app, db_url="sqlite://db.sqlite3", modules={"models": ["valence_api.models"]}
    )
