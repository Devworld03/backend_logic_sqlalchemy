from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from database_connection import get_db 
from models import Student,Task
from schema import StudentCreate, StudentUpdate
from schema import TaskCreate

# APIRouter → Creates a separate router for student APIs.
# Depends → Injects the database session.
# Session → Type hint for SQLAlchemy session.
# get_db → Gives us a database session.
# Student → SQLAlchemy model.
# StudentCreate → Request body validation.

router=APIRouter(prefix="/students",tags=["Students"])

@router.post("/")
def create_student(student:StudentCreate,db:Session=Depends(get_db)):
    new_student=Student(
        name=student.name ,
        email=student.email 

    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {
    "message": "Student created successfully.",
    "student": {
        "id": new_student.id,
        "name": new_student.name,
        "email": new_student.email
    }
}

@router.get('/')
def get_students(db:Session=Depends(get_db)):
    student=db.query(Student).all()
    return student
@router.get('/{id}')
def get_student_by_id(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first() 
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
@router.put('/{id}')
def update_student(id:int,student_data:StudentUpdate,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first() 
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    if student_data.name is not None:
        student.name = student_data.name

    if student_data.email is not None:
        student.email = student_data.email 
    db.commit() 
    db.refresh(student)
    return {
        "messagae":"Student updated succesfully",
        "student":{
            "id":student.id,
            "name":student.name,
            "email":student.email 
        }
    }
@router.delete('/{id}')
def delete_student(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first() 
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db.delete(student)
    db.commit() 
    return{
        "message":"student data deleted succesfully"
    }
@router.post('/{id}/tasks')
def create_task(id:int,task:TaskCreate,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first() 
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    new_task=Task(  
        title=task.title,
        description=task.description,
        status=task.status, 
        student_id=student.id
        )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

@router.get('/{id}/tasks')

def student_all_tasks(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    return student.tasks
