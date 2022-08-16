from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import valence_api


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    valence_api.models.register(app)
    return app
