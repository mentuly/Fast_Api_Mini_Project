from sqlmodel import Field,SQLModel


class PKMixin(SQLModel):
    pk:str = Field(primary_key=True)