from typing import List
from models.users import User, UserCreate, UserRead, UserUpdate
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session, select
from init_db import get_db
from utils.encrypt import verify_password, encrypt_password

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = User(**user.dict())
    print("DEBUG: user class:", User)
    print("DEBUG: user.__table__:", getattr(User, "__table__", None))
    encrypted_password = encrypt_password(user.password)
    user.password = encrypted_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=List[UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.exec(select(User).offset(skip).limit(limit)).all()
    return users

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@router.post("/login")
def login_user(username: str = Body(...), password: str = Body(...), db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.username == username)).one_or_none()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful", "user_id": user.id}

