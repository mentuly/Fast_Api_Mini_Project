from sqlmodel import SQLModel



class TokenData(SQLModel):
    access_token: str
    token_type: str



class Token(SQLModel):
    username: str | None = None
