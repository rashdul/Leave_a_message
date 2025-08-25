from fastapi import FastAPI, Depends, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models, database, crud

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)



@app.post("/leave_a_message")
def leave_message(
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(database.get_db)
):
    new_msg = crud.create_message(db, first_name, last_name, email, message)
    return JSONResponse(content={"status": "Message received", "id": new_msg.id})

