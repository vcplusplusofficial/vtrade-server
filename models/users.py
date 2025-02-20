from fastapi import APIRouter
from sqlalchemy import Column
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

router = APIRouter()
class UserBase (SQLModel):
    username: str = Field(sa_column=Column("username", unique=True))
    email: str = Field(sa_column=Column("email", unique=True))
    password: str = Field(sa_column=Column("password"))
    created_at: datetime = Field(sa_column=Column("created_at"), default_factory=datetime.now)
    modified_at: datetime = Field(sa_column=Column("modified_at"), default_factory=datetime.now)
    first_name: Optional[str] = Field(sa_column=Column("first_name"), default=None)
    last_name: Optional[str] = Field(sa_column=Column("last_name"), default=None)

class User (UserBase, table=True):
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





