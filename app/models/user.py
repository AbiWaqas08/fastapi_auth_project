from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    # TAble Namein mysql
    __tablename__ = "users"

    # Auto increment primary key
    id = Column(Integer, nullable=False,primary_key=True, index=True)
    # User name
    name = Column(String(100), nullable=False)
    # Unique email
    email = Column(String(100), unique=True, index=True)
    # hashed password
    password = Column(String(150), nullable=False)