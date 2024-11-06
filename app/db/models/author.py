from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from ..mixin import PKMixin



class Author(PKMixin,SQLModel,table=True):
    name:str
    email:EmailStr = Field(unique=True)
    bio:str|None = Field(max_length=50)
    password:str



