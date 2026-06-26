from sqlalchemy import Column,Integer,String,ForeignKey 
from sqlalchemy.orm import relationship 
from database_connection import engine

from database_connection import Base 

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    tasks=relationship("Task",back_populates="student")
class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    status=Column(String,default="Pending")
    student_id=Column(Integer,ForeignKey("students.id"))
    student=relationship("Student",back_populates="tasks")


