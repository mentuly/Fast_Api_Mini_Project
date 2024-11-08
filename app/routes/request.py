from fastapi import APIRouter, HTTPException,Depends
from ..db import ArticleRequest,Article
from sqlmodel import select,Session
from ..utils import get_session
from typing import Annotated



request_router=APIRouter(prefix="/request",tags=["Request"])



@request_router.post("")
def request(data:ArticleRequest,session:Annotated[Session,Depends(get_session)]):
    response=[]
    keywords=data.keywords
    end_date=data.end_date
    start_date=data.start_date
    articles = session.scalars(select(Article).where(Article.published_at>=start_date,Article.published_at<=end_date))
    if not articles:
        raise HTTPException(status_code=402,detail="No article matches your request")
    for article in articles:
        if any(w in article.content for w in keywords):
            response.append(article)
    return response