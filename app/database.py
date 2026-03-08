# app/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()

# Read DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

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



