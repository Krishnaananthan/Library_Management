from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    password:str
    role:str

class BookCreate(BaseModel):
    title:str
    author:str
    
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    available: bool
    count:int
