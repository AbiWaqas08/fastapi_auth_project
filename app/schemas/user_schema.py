# app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr

# Signup request schema
class UserSignup(BaseModel):
    name: str
    email: EmailStr # validate email format automatically
    password: str 

# Login request schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    