from fastapi import APIRouter, Depends, HTTPException
from app.schemas.task import Task 
from sqlalchemy.orm import Session
from . import schemas, services
from ..database import SessionLocal
import logging
import services.task_service 


router = APIRouter(prefix="/tasks", tags=["Tasks"])
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.task.Task])
def read_tasks(db: Session = Depends(get_db)):
    logger.info("Fetching all tasks")
    return services.task_service.get_tasks(db)

@router.get("/{task_id}", response_model=schemas.task.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = services.task_service.get_task(db, task_id)
    if not task:
        logger.warning(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=schemas.task.Task)
def create_task(task: schemas.task.TaskCreate, db: Session = Depends(get_db)):
    logger.info("Creating a new task")
    return services.task_service.create_task(db, task)

@router.put("/{task_id}", response_model=schemas.task.Task)
def update_task(task_id: int, task_data: schemas.task.TaskUpdate, db: Session = Depends(get_db)):
    updated = services.task_service.update_task(db, task_id, task_data)
    if not updated:
        logger.warning(f"Task {task_id} not found for update")
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", response_model=schemas.task.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = services.task_service.delete_task(db, task_id)
    if not deleted:
        logger.warning(f"Task {task_id} not found for deletion")
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted
