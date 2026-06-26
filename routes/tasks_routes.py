from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database_connection import get_db
from models import Student,Task
from schema import TaskCreate

router2=APIRouter(prefix='/tasks',tags=["Tasks"])

@router2.get('/')
def get_tasks(db:Session=Depends(get_db)):
    tasks=db.query(Task).all()
    return tasks

@router2.get('/{id}')

def get_task_by_id(id:int,db:Session=Depends(get_db)):
    tasks=db.query(Task).filter(Task.id==id).first()
    return tasks

@router2.put('/{id}')

def update_task(id:int,task:TaskCreate,db:Session=Depends(get_db)):
    query=db.query(Task).filter(Task.id==id).first()
    if query is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found")
    if task.title is not None:
         query.title=task.title
    if task.description is not None:
         query.description=task.description 
    if task.status is not None:
         query.status=task.status 
    db.commit() 
    db.refresh(query)
    return {
         "message":"task updated succefully",
         "info":{
              "title":query.title,
              "description":query.description, 
              "status":query.status
         }
    } 

@router2.delete('/{id}')
def delete_task(id :int,db:Session=Depends(get_db)):
     task=db.query(Task).filter(Task.id==id).first()
     if task is None:
          raise HTTPException(
               status_code=404,
               detail="task is not there"
          )
     db.delete(task)
     db.commit()
     return{
          "message":"task deleted successfully"
     }