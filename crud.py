from sqlalchemy.orm import Session
import models
import database
import crud

def create_message(db: Session, first_name: str, last_name: str, email: str, message: str):
    new_msg = models.Message(first_name=first_name, last_name=last_name, email=email, message=message)
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg
