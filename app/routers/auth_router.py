# app/routers/auth_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import session

from app.schemas.user_schema import UserLogin, UserSignup
from app.models.user import User
from app.database import Sessionlocal
from app.services.auth_service import create_user
from app.core.security import varify_password, create_access_token

# create router with prefix /auth
router = APIRouter(prefix="/auth")

# dependency to get DB session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# signup API
@router.post("/signup")
def signup(user: UserSignup, db: session = Depends(get_db)):
    # check if user already exists
    existing_user = db.query(User).filer(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email Already registered.")
    
    # create newe user
    create_user(db, user.name, user.email, user.password)
    return {"message: User created sccessfully."}

# Login API
@ router.post("/login")
def login(user: UserLogin, db:session = Depends(get_db)):
    # fetch user by email
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # varify password
    if not varify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # generate JWT token
    token = create_access_token({"user_id": db_user.id})
    return {"access_token": token, "token_type": "baerer"}
