from __future__ import annotations

from tortoise import fields
from tortoise.models import Model

import valence_api


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32)
    display_name = fields.CharField(max_length=64)
    password_hash = fields.CharField(max_length=128)

    async def verify_password(self, password: str) -> bool:
        return valence_api.auth.password.verify_password(
            password, self.password_hash
        )

    @classmethod
    async def authenticate_user(cls, username: str, password: str) -> bool | User:
        user = await cls.get(username=username)

        if not user:
            return False
        if not user.verify_password(password):
            return False
        return user
