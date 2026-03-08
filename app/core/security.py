# app/core/security.py

# for hashing password
from passlib.context import CryptContext
# for jwt token
from jose import jwt
from datetime import datetime, timedelta

# password hashing configration
pwd_context = CryptContext(schemes=['argon2'], deprecated="auto")

# jwt configration
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# hash plain passowrd before storing in DB
def hash_password(password: str):
    # truncate to 72 characters
    password = password[:72]
    return pwd_context.hash(password)

# verify plain password against hash password
def varify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# create JWT access token
def create_access_token(data: dict):
    to_encode = data.copy()
    # expiry time
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    # add expiry to payload
    to_encode.update({"exp": expire})
    # encode JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt