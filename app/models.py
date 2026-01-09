from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    # password=Column(String)
    role=Column(String)


class Book(Base):
    __tablename__ = "Books"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,unique=True)
    author=Column(String)
    available=Column(Boolean,default=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
