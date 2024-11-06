from sqlmodel import SQLModel,create_engine,Session


class Config:
    ENGINE = create_engine("sqlite:///mydb.db", echo=True)
    SESSION = Session(ENGINE)
    BASE = SQLModel