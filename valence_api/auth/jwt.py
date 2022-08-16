from datetime import datetime, timedelta

from jose import JWTError, jwt

import valence_api

JTW_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, valence_api.env.SECRET_KEY, algorithm=JTW_ALGORITHM
    )
    return encoded_jwt
