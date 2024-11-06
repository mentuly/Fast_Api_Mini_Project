# from typing import Annotated
# from datetime import datetime, timedelta, timezone
# from fastapi import Depends, FastAPI, HTTPException, status, APIRouter

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from uvicorn import run
# from sqlmodel import SQLModel, Field, create_engine
# from pydantic import BaseModel, Field as PDField
# from sqlalchemy.orm import sessionmaker, Session
# import hashlib
# import jwt
# from jwt.exceptions import InvalidTokenError
# from passlib.context import CryptContext
# from ..db import Token,Author


# app = FastAPI()

# SECRET_KEY = "d29b0518d40de3bdc7cd369265bb4ff3daec082666f0923979ae8d44f2c8946f"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# ENGINE = create_engine("sqlite:///mydb.db", echo=True)
# SESSION = sessionmaker(bind=ENGINE)

# OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
# PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

# auth_router = APIRouter(tags=["Authentication"])



# def get_password_hash(password: str) -> str:
#     return PWD_CONTEXT.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return PWD_CONTEXT.verify(plain_password,hashed_password)
 
 
