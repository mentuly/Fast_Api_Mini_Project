from typing import List
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

from ..mixin import PKMixin


class Author(PKMixin, SQLModel, table=True):
    name: str
    email: EmailStr = Field(unique=True)
    bio: str | None = Field(max_length=50)
    password: str

    articles: List["Article"] = Relationship(back_populates="author")
    comments: List["Comment"] = Relationship(back_populates="author")
