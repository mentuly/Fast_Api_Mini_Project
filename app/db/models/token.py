from sqlmodel import SQLModel


class Token(SQLModel):
    username: str | None = None
