from sqlmodel import SQLModel, Relationship, Field
from ..mixin import PKMixin, PUBMixin


class Comment(PKMixin, PUBMixin, SQLModel, table=True):
    content: str

    author: "Author" = Relationship(back_populates="comments")
    author_id: int = Field(foreign_key="author.id")
