from fastapi import FastAPI
from routes.student_routes import router
from database_connection import engine
from models import Base
from routes.tasks_routes import router2
app=FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(router2)