from fastapi import APIRouter

import valence_api

router = APIRouter(
    prefix="/user",
    tags=["users"],
)


@router.get("/me", response_model=valence_api.schemas.user.User)
def get_current_user():
    pass
