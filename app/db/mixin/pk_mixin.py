from typing import Annotated
from sqlmodel import Field, SQLModel


class PKMixin(SQLModel):
    id: Annotated[int, Field(primary_key=True, exclude=True)]
