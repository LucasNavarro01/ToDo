from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services import task_service
from app.database import SessionLocal

router = APIRouter(prefix='/tasks', tags=['Tasks'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/', response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)

@router.get('/{task_id}', response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task

@router.post('/', response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)

@router.put('/{task_id}', response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    updated = task_service.update_task(db, task_id, task_data)
    if not updated:
        raise HTTPException(status_code=404, detail='Task not found')
    return updated

@router.delete('/{task_id}', response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = task_service.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail='Task not found')
    return deleted
