from sqlmodel import SQLModel,Relationship
from typing import List
from .author import Author
from ..mixin import PKMixin,PUBMixin



class Article(PKMixin,PUBMixin,SQLModel,table=True):
    title:str
    content:str
    author:Author = Relationship(back_populates="article")
    tags:str