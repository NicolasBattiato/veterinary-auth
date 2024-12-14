import sys
from app.domain.user import UserCreate, UserLogin
from fastapi import APIRouter, Depends, HTTPException
from app.core.security import create_access_token, verify_password, create_refresh_token
from app.infrastructure.database import get_db
from sqlalchemy.orm import Session
from app.infrastructure.repositories.user import UserRepo
from app.services.user import register_user, delete_user, activate_user

router = APIRouter()

@router.post("/login")

async def login(user: UserLogin, db: Session = Depends(get_db)):
    user_db = UserRepo.get_user_by_email(db, user.email)
    if not user_db or not verify_password(user.password, user_db.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    access_token = create_access_token(user_db.to_access_token())
    return {"access token": access_token, "token": "Bearer"}
    
@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail= "Email Already Registered")
    
    return {"message": "User Created Succesfully"}

@router.post("/verify/{user_id}")
async def verify_user(user_id: int, db: Session = Depends(get_db)):
    user = UserRepo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail= "User Not Found")
    user = activate_user(db, user)
    return {"message": "User Verified Succesfully"}

@router.delete("/delete/{user_id}")
async def soft_delete(user_id: int, db: Session = Depends(get_db)):
    user = UserRepo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    delete_user(db, user)
    return {"message": "User Deleted Succesfully"}

@router.post("/refresh")
async def refresh_token(user: UserLogin, db : Session = Depends(get_db)):
    db_user = UserRepo.get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    refresh_token = create_refresh_token(db_user.to_access_token())
    return {"refresh_token": refresh_token}

    
