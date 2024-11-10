from fastapi import APIRouter, HTTPException, Depends, status

from sqlmodel import select, update, Session
from typing import Annotated

from ..db import Comment, Author
from ..utils import get_session, get_current_user
from ..logging.middleware import request_logging_dependency


comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
    dependencies=[Depends(request_logging_dependency)],
)


@comment_router.get("/all_comment")
def all_comment(
    session: Annotated[Session, Depends(get_session)]
):
    """
    See all comments
    """
    resp = []
    comments = session.scalars(select(Comment)).all()
    for comment in comments:
        resp.append(comment)
    return resp


@comment_router.post("/create", status_code=status.HTTP_201_CREATED)
def comment(
    data: Comment,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Create a comment with all the information:

    - **published at**: date when this comment was published (cannot be in future,default date - todays date)
    - **content**: content of a comment
    - **author id**: id of an author who wrote this comment
    """
    comment = Comment(**data.model_dump())
    session.add(comment)
    return "Created"


@comment_router.delete("/all")
def del_all_comment(
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Delete all comments
    """
    comments = session.scalars(select(Comment)).all()
    for comment in comments:
        session.delete(comment)
        return "Deleted"


@comment_router.get("/{id}")
def one_comment(
    id: int, 
    session: Annotated[Session, Depends(get_session)]
):
    """
    See one comment with details:

    - **id**: comment's id
    """
    comment = session.scalar(select(Comment).where(Comment.id == id))
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@comment_router.put("/{id}")
def update_comment(
    id: int,
    data: Comment,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Update one comment:

    - **id**: comment's id

    - **published at**: new date (cannot be in future,default date - todays date)
    - **content**: new content
    - **author id**: id of an author who wrote this comment
    """
    comment = session.scalar(select(Comment).where(Comment.id == id))
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    upd = update(Comment).where(Comment.id == id).values(**data.model_dump())
    session.execute(upd)
    return comment


@comment_router.delete("/delete_one/{id}")
def del_one_comment(
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Delete one comment:

    - **id**: comment's id
    """
    comment = session.scalar(select(Comment).where(Comment.id == id))
    if not comment:
        raise HTTPException(status_code=404, detail="No comment with this id")
    session.delete(comment)
    return comment
