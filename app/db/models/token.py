from sqlmodel import SQLModel
from ..mixin import PKMixin


class Token(PKMixin,SQLModel,table=False):
    token:str
