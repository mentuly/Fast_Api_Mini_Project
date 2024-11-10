from typing import Annotated

from sqlmodel import select, update, Session
from fastapi import APIRouter, HTTPException, Depends

from ..utils import get_session, get_current_user
from ..db import Author
from ..logging.middleware import request_logging_dependency

author_router = APIRouter(
    prefix="/author",
    tags=["Author"],
    dependencies=[Depends(request_logging_dependency)],
)


@author_router.get("/all")
def all_authors(
    session: Annotated[Session, Depends(get_session)],
):
    """
    See all authors
    """
    resp = []
    authors = session.scalars(select(Author)).all()
    for author in authors:
        resp.append(author)
    return resp


@author_router.delete("/delete/{id}")
def del_author(
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Delete one author:

    - **id**: author's id
    """
    author = session.scalar(select(Author).where(Author.id == id))
    if not author:
        raise HTTPException(status_code=404, detail="No author with this id")
    session.delete(author)
    return "Deleted"


@author_router.delete("/delete_all")
def del_all_authors(
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Delete all authors
    """
    authors = session.scalars(select(Author)).all()
    for author in authors:
        session.delete(author)
        return "Deleted"


@author_router.get("/{id}")
def one_author(
    id: int, 
    session: Annotated[Session, Depends(get_session)]):
    """
    See one author with details:

    - **id**: author's id
    """
    author = session.scalar(select(Author).where(Author.id == id))
    if not author:
        raise HTTPException(status_code=404, detail="No author with this id")
    return author


@author_router.put("/{id}")
def update_author(
    id: int,
    data: Author,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    """
    Update one author:

    - **id**: author's id

    - **name**: new name
    - **e-mail**: new e-mail (should be valid e-mail adress,should not be already registered)
    - **bio**: new author's biography (not required,max length - 50)
    - **password**: change password
    """
    author = session.scalar(select(Author).where(Author.id == id))
    if not author:
        raise HTTPException(status_code=404, detail="No author with this id")
    upd = update(Author).where(Author.id == id).values(**data.model_dump())

    session.execute(upd)
    return author
