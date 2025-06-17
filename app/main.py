from fastapi import FastAPI
from app.routers import api_router
from app.database import Base, engine
import logging
from app.config import settings

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
Base.metadata.create_all(bind=engine)

app = FastAPI(title='ToDo API')
app.include_router(api_router)
