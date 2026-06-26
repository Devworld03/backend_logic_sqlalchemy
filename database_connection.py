from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
engine=create_engine(
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE}"
       )
connection=engine.connect()
SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)
   
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()
