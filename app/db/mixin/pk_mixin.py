from sqlmodel import Field,SQLModel
from typing import Annotated



class PKMixin(SQLModel):
    id:Annotated[int, Field(primary_key=True,exclude=True)]