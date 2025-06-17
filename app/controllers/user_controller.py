
from fastapi import HTTPException
from app.services import user_service

def get_users_controller():
    return user_service.fetch_all_users()

def get_user_controller(user_id: int):
    user = user_service.fetch_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
