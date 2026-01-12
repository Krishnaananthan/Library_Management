from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud,schemas


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
def add_book(title:str,author:str,count:int,user_id:int,db:Session=Depends(get_db)):
    return crud.add_book(db,title,author,count,user_id)

@router.post("/buybook")
def buy_book(book_id:int,user_id:int,db:Session=Depends(get_db)):
    return crud.buy_book(db,book_id,user_id)
    
@router.get("/getUsers")
def all_user(db:Session=Depends(get_db)):
    return crud.all_user(db)

@router.get("/getBooks")
def all_books(db:Session=Depends(get_db)):
    return crud.all_books(db)

@router.delete("/delBook/{del_id}")
def del_book(del_id:int,db:Session=Depends(get_db)):
    del_book = crud.del_book(db,del_id)
    return {"Message":"Book deleted Successfully"}

@router.put("/updateBook/{update_book_id}")
def update_book(update_book_id:int,user:schemas.BookCreate,db:Session=Depends(get_db)):
    try:
        update_book=crud.update_book(db,update_book_id = update_book_id,user=user)
        return update_book
    
    except Exception as e:
        print("There is something is mistake")
    
    
# @router.put("/update")
# def update_user(update_id:int,user:schemas.UserCreate,db:Session=Depends(get_db)):
#     try:
#         db_user = crud.update_user(db,update_id=update_id,user=user)
#         print(db_user,"l")
#         if db_user is None:
#             raise HTTPException(status_code=404, detail="User not found")
#         return "db_user"
#     except Exception as e:
#         import traceback
#         print(traceback.format_exc())