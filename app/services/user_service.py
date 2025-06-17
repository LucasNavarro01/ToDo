
from app.repositories import user_repository

def fetch_all_users():
    return user_repository.get_all_users()

def fetch_user_by_id(user_id: int):
    return user_repository.get_user_by_id(user_id)
