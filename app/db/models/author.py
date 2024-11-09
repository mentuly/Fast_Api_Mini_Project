from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr,model_validator
from typing import List

from ..mixin import PKMixin
from ...logging.logg import validations_logger
from .utils import get_password_hash




class Author(PKMixin,SQLModel,table=True):
    name:str
    email:EmailStr = Field(unique=True)
    bio:str|None = Field(max_length=50)
    password:str

    articles:List["Article"] = Relationship(back_populates="author")
    comments:List["Comment"] = Relationship(back_populates="author")

    
    @model_validator(mode="after")
    def hash_password(self):
        self.password=get_password_hash(self.password)
        validations_logger.info("Model: AuthorData, Field: password, Result: Hash Created")
        return self
        

