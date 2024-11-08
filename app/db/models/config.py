from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker


class Config:
    ENGINE = create_engine("sqlite:///mydb.db", echo=True)
    SESSION = sessionmaker(ENGINE)
    BASE = SQLModel
