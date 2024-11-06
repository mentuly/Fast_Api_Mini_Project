from sqlmodel import SQLModel, Field
from ..mixin import PKMixin


class Token(PKMixin,SQLModel,table=True):
    token:str
