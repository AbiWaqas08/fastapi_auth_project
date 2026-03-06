# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MYSQL database URL
DATABASE_URL = ""

# CREATE SQLAlchemy engine to connect MYSQL
engine = create_engine(DATABASE_URL)

# Create a session to intreract with the database
Sessionlocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()