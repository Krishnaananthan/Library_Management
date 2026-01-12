
from fastapi import FastAPI, Depends
from app.database import Base, engine
from app.models import User, Book
from app.routers import users

from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management - Role Based")


app.include_router(users.router)



@app.get("/")
def get():
    return {"Message":"Library Manangement"}