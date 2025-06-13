from fastapi import FastAPI
from .routers import task_router
from .database import Base, engine
import logging
from .config import settings

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo API")
app.include_router(task_router.router)
