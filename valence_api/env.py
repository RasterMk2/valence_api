import os

import dotenv
from loguru import logger

dotenv.load_dotenv()


def get_env(key: str) -> str:
    env = os.getenv(key)
    if env is not None:
        return env
    else:
        logger.critical(f'Required environment variable "{key}" not found.')
        exit()


SECRET_KEY = get_env("SECRET_KEY")
