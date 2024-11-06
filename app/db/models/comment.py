from sqlmodel import SQLModel,Relationship
from .author import Author
from ..mixin import PKMixin,PUBMixin



class Comment(PKMixin,PUBMixin,SQLModel,table=True):
    author:Author = Relationship(back_populates="article")
    content:str