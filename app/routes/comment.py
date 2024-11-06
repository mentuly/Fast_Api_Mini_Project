from fastapi import APIRouter, HTTPException
from ..db import Config,Comment
from sqlalchemy import select

Session=Config.SESSION


comment_router = APIRouter(prefix="/comments", tags=["Comments"])



@comment_router.get("/all_comment")
def all_comment():
    with Session() as session:
        articles = session.scalars(select(Comment)).all()
        return articles


@comment_router.post("/create")
def comment(data:Comment):
    with Session.begin() as session:
        article = Comment(**data.model_dump())
        session.add(article)


@comment_router.delete("/all")
def del_all_comment():
    with Session.begin() as session:
        comments = session.scalars(select(Comment)).all()
        session.delete(comments)
        return "Deleted"


@comment_router.get("/{id}")
def one_comment(id:int):
    with Session() as session:
        comment=session.scalar(select(Comment).where(Comment.id==id))
        if not comment:
            raise HTTPException(status_code=400,detail="")
        return comment
    

@comment_router.put("/{id}")
def update_comment(id:int):
    with Session() as session:
        comment=session.scalar(select(Comment).where(Comment.id==id))
        if not comment:
            raise HTTPException(status_code=404, detail="Comment not found")
        comment.author = Comment.author
        comment.content = Comment.content
        session.add(comment)
        session.commit()
        return comment