from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User,Book
from app import schemas


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

def add_book(db:Session,title:str,author:str,count:int,user_id:int):
    check_admin(db,user_id)

    book=Book(title=title,author=author,count=count)
    db.add(book)
    db.commit()
    return book

def buy_book(db:Session,book_id:int,user_id:int):
    book=db.query(Book).filter(Book.id == book_id,Book.available==True,Book.count>=1).first()

    if not book:
        raise HTTPException(status_code=404,detail="Book not Founds")

    # book.available=False
    book.count -=1
    if(book.count == 0):
        book.available=False
    book.count = Book.count -1 
    book.owner_id=user_id
    db.commit()
    return book

def all_user(db:Session):
    return db.query(User).all()

def all_books(db:Session):
    return db.query(Book).all()

def del_book(db:Session,delete_id:int):
    del_book=db.query(Book).filter(Book.id==delete_id).first()
    db.delete(del_book)
    db.commit()
    return del_book

def update_book(db:Session,update_book_id:int,user: schemas.BookCreate):
    update_book=db.query(Book).filter(Book.id == update_book_id).first()

    if update_book:
        update_book.title=user.title
        update_book.author=user.author
        db.commit()
        # db.refresh(update_book)
        print(update_book,"kk")
        return update_book
    return None



# def update_user(db: Session, update_id: int, user: schemas.UserCreate):
#     db_user = db.query(models.User).filter(models.User.id == update_id).first()
#     if db_user:
#         db_user.name = user.name
#         db_user.email = user.email
       
#         db.commit()
#         db.refresh(db_user)
#         return db_user
#     return None

