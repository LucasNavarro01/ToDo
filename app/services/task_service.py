from sqlalchemy.orm import Session
from .. import models, schemas

def get_tasks(db: Session):
    return db.query(models.task.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.task.Task).filter(models.task.Task.id == task_id).first()

def create_task(db: Session, task: schemas.task.TaskCreate):
    db_task = models.task.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_data: schemas.task.TaskUpdate):
    task = get_task(db, task_id)
    if task:
        for key, value in task_data.dict().items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task
