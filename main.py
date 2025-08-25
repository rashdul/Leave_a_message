from fastapi import FastAPI, Depends, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models, database, crud
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


# Allow your Netlify site to talk to your API
origins = [
    "https://rdulijan.com",  # replace with your actual Netlify domain
    "http://localhost:5500",  # useful for local dev if you test from file:// or localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] if you want to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

