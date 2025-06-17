from fastapi import APIRouter
from app.routers.v1 import task_router, user_router

api_router = APIRouter()
api_router.include_router(task_router.router, prefix="/v1/tasks", tags=["tasks"])
api_router.include_router(user_router.router, prefix="/v1/users", tags=["users"])
