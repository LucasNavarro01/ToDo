
from fastapi import APIRouter
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return user_controller.get_users_controller()

@router.get("/{user_id}")
def get_user(user_id: int):
    return user_controller.get_user_controller(user_id)
