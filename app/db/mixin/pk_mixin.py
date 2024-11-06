from sqlmodel import Field,SQLModel


class PKMixin(SQLModel):
    id:str = Field(primary_key=True)