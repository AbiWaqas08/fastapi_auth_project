# app/servises/auth_service.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password


# function to create a new user in the database
def create_user(db:Session, name: str, email: str, password: str):
    # hash password before storing
    hashed = hash_password(password)
    user = User(
        name = name,
        email = email,
        password = hashed
    )

    # add user to db session
    db.add(user)
    # commit transaction to save user
    db.commit()
    # refresh object to get generated field like id
    db.refresh(user)
    return(user)