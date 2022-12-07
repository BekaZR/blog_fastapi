from fastapi import APIRouter, Depends, Request

from sqlalchemy.orm import Session

from schemas.users import UserIn, UserOut

from models.users import User

from core.dependices import get_db

from services.hash_password import get_password_hash


router = APIRouter()

@router.post('/registration/', response_model=UserOut)
def registration(user: UserIn, db: Session = Depends(get_db)):
    user_db = User(username=user.username, password=get_password_hash(user.password))
    
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    
    return user_db