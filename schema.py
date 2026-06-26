from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    name:str
    email:str
class StudentUpdate(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None 

class TaskCreate(BaseModel):
    title:str 
    description:Optional[str]=None 
    status:str 
