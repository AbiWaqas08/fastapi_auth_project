# app/models/user.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    # Table name in mysql
    __tablename__ = "Users"

    # Auto increment primary key
    id = Column(Integer, primary_key=True, index=True)

    # User name
    name = Column(String(100), nullable=False)

    # Unique Email
    email = Column(String(150), unique=True, index=True, nullable=False)

    # Hashed password
    password = Column(String(256), nullable=False)