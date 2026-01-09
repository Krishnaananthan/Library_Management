from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/createUsers")
def create_user(username:str,role:str,db: Session=Depends(get_db)):
    return crud.create_user(db,username,role)

@router.post("/addbook")
def add_book(title:str,author:str,user_id:int,db:Session=Depends(get_db)):
    return crud.add_book(db,title,author,user_id)

@router.post("/buybook")
def buy_book(book_id:int,user_id:int,db:Session=Depends(get_db)):
    return crud.buy_book(db,book_id,user_id)
    
@router.get("/getUsers")
def all_user(db:Session=Depends(get_db)):
    return crud.all_user(db)
@router.get("/getBooks")
def all_books(db:Session=Depends(get_db)):
    return crud.all_books(db)