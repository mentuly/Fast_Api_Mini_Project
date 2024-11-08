from fastapi import APIRouter, HTTPException,Depends,status
from ..db import Comment
from sqlmodel import select,update,Session
from typing import Annotated
from ..utils import get_session


comment_router = APIRouter(prefix="/comments", tags=["Comments"])


@comment_router.get("/all_comment")
def all_comment(session:Annotated[Session,Depends(get_session)]):
    resp=[]
    comments = session.scalars(select(Comment)).all()
    for comment in comments:
        resp.append(comment)
    return resp


@comment_router.post("/create",status_code=status.HTTP_201_CREATED)
def comment(data:Comment,session:Annotated[Session,Depends(get_session)]):
    comment = Comment(**data.model_dump())
    session.add(comment)
    return "Created"

@comment_router.delete("/all")
def del_all_comment(session:Annotated[Session,Depends(get_session)]):
    comments = session.scalars(select(Comment)).all()
    for comment in comments:
        session.delete(comment)
        return "Deleted"


@comment_router.get("/{id}")
def one_comment(id:int,session:Annotated[Session,Depends(get_session)]):
    comment=session.scalar(select(Comment).where(Comment.id==id))
    if not comment:
        raise HTTPException(status_code=404,detail="Comment not found")
    return comment
    

@comment_router.put("/{id}")
def update_comment(id:int,data:Comment,session:Annotated[Session,Depends(get_session)]):
    comment=session.scalar(select(Comment).where(Comment.id==id))
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    upd=update(Comment).where(Comment.id==id).values(**data.model_dump())
    session.execute(upd)
    return comment
    

@comment_router.delete("/delete_one/{id}")
def del_one_comment(id:int,session:Annotated[Session,Depends(get_session)]):
    comment=session.scalar(select(Comment).where(Comment.id==id))
    if not comment:
        raise HTTPException(status_code=404,detail="No comment with this id")
    session.delete(comment)
    return comment