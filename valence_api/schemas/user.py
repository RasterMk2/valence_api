from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    display_name: str
