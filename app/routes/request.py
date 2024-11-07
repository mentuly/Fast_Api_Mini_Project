from fastapi import APIRouter, HTTPException
from ..db import Config,ArticleRequest,Article
from sqlmodel import select


Session=Config.SESSION
request_router=APIRouter(prefix="/request",tags=["Request"])



@request_router.post("")
def request(data:ArticleRequest):
    with Session() as session:
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