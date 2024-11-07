from fastapi import APIRouter,HTTPException,status
from ..db import Config,Article
from sqlmodel import select,update

Session=Config.SESSION


article_router=APIRouter(prefix="/articles", tags=["Article"])

@article_router.get("/all")
def all_articles():
    with Session() as session:
        articles = session.scalars(select(Article)).all()
        return articles

@article_router.post("/create",status_code=status.HTTP_201_CREATED)
def create_article(data:Article):
    with Session.begin() as session:
        article = Article(**data.model_dump())
        session.add(article)
        return "Created"
    

@article_router.delete("/delete_all")
def del_all_articles():
    with Session.begin() as session:
        articles = session.scalars(select(Article)).all()
        for article in articles:
            session.delete(article)
            return "Deleted"
    

@article_router.get("/{id}")
def one_article(id:int):
    with Session() as session:
        article=session.scalar(select(Article).where(Article.id==id))
        if not article:
            raise HTTPException(status_code=404,detail="No article with this id")
        return article



@article_router.put("/{id}")
def upd_article(id:int,data:Article):
    with Session.begin() as session:
        article= session.scalar(select(Article).where(Article.id==id))
        if not article:
            raise HTTPException(status_code=404,detail="No article with this id")
        upd = update(Article).where(Article.id == id).values(
            title=data.title,
            content=data.content,
            author=data.author,
            tags=data.tags
            )
        
        session.execute(upd)
        return article



@article_router.delete("/delete_one/{id}")
def del_one_article(id:int):
    with Session() as session:
        article=session.scalar(select(Article).where(Article.id==id))
        if not article:
            raise HTTPException(status_code=404,detail="No article with this id")
        session.delete(article)
        return article
        
        
    
