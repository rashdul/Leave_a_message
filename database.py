from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import models
import database
import crud

DATABASE_URL = "postgresql://postgres:Rraa%40113355@localhost:5432/leave_a_message"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency to use in FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
