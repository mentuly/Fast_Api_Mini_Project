from sqlmodel import Field,SQLModel


class PKMixin(SQLModel):
    id:int = Field(primary_key=True)