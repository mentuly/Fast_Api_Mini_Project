from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select, update, Session
from ..db import Article, Author
from ..utils import get_session, get_current_user
from ..logging.middleware import request_logging_dependency


article_router = APIRouter(
    prefix="/articles",
    tags=["Article"],
    dependencies=[Depends(request_logging_dependency)],
)


@article_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_article(
    data: Article,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    article = Article(**data.model_dump())
    session.add(article)
    return "Created"


@article_router.delete("/delete_all")
def del_all_articles(
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    articles = session.scalars(select(Article)).all()
    for article in articles:
        session.delete(article)
    return "Deleted"


@article_router.put("/{id}")
def upd_article(
    id: int,
    data: Article,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    article = session.scalar(select(Article).where(Article.id == id))
    if not article:
        raise HTTPException(status_code=404, detail="No article with this id")
    upd = update(Article).where(Article.id == id).values(**data.model_dump())
    session.execute(upd)
    return article


@article_router.delete("/delete_one/{id}")
def del_one_article(
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[Author, Depends(get_current_user)],
):
    article = session.scalar(select(Article).where(Article.id == id))
    if not article:
        raise HTTPException(status_code=404, detail="No article with this id")
    session.delete(article)
    return article
