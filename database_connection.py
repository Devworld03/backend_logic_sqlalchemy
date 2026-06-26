from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DB_USERNAME="postgres"
DB_PASSWORD="123456789"
HOST="localhost"
PORT=5432
DATABASE="student_db"
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