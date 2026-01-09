from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User, Book


def create_user(db:Session,username:str,role:str):
    
    user=User(username=username,role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def check_admin(db:Session,user_id:int):
    user=db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not Found")
    if user.role != "admin":
        raise HTTPException(status_code=403,detail="not Admin")
    return user

def add_book(db:Session,title:str,author:str,user_id:int):
    check_admin(db,user_id)

    book=Book(title=title,author=author)
    db.add(book)
    db.commit()
    return book
def buy_book(db:Session,book_id:int,user_id:int):
    book=db.query(Book).filter(Book.id == book_id,Book.available==True).first()

    if not book:
        raise HTTPException(status_code=404,detail="Book not Founds")

    book.available=False
    book.owner_id=user_id
    db.commit()
    return book

def all_user(db:Session):
    return db.query(User).all()

def all_books(db:Session):
    return db.query(Book).all()


