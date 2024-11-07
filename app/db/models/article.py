from sqlmodel import SQLModel,Relationship,Field
from ..mixin import PKMixin,PUBMixin



class Article(PKMixin,PUBMixin,SQLModel,table=True):
    title:str
    content:str
    tags:str

    author:"Author" = Relationship(back_populates="articles")
    author_id:int = Field(foreign_key="author.id")