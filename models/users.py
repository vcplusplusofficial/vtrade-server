from fastapi import APIRouter
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

router = APIRouter()
class UserBase (SQLModel):
    username: str
    email: str
    password: str = None
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class User (UserBase, Table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate (UserBase):
    pass

class UserRead (UserBase):
    id: int

    class Config:
        from_attributes = True

class UserUpdate (UserBase):
    username: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    modified_at: datetime = Field(default_factory=datetime.now)





