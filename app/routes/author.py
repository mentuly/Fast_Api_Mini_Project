from ..db import Config, Author
from sqlmodel import select, update
from fastapi import APIRouter,HTTPException

author_router =APIRouter(prefix="/author", tags=["Author"])

Session=Config.SESSION


@author_router.get("/all")
def all_authors():
    with Session() as session:
        authors = session.scalars(select(authors)).all()
        return authors

# @author_router.get("/create")
# def create_author(data:Author):
#     with Session.begin() as session:
#         author = Author(**data.model_dump())
#         session.add(author)
#         return "Created"

@author_router.delete("/delete")
def del_author():
    with Session.begin() as session:
        author = session.scalar(select(Author))
        if not author:
            raise HTTPException(status_code=404,detail="No author with this id")
        session.delete(author)
        return "Deleted"


@author_router.delete("/delete_all")
def del_all_authors():
    with Session.begin() as session:
        authors = session.scalars(select(Author)).all()
        session.delete(authors)
        return "Deleted"
    

@author_router.get("/{id}")
def one_author(id:int):
    with Session() as session:
        author=session.scalar(select(Author).where(Author.id==id))
        if not author:
            raise HTTPException(status_code=404,detail="No author with this id")
        return author

@author_router.put("/{id}")
def update_author(id:int,data: Author):
    with Session.begin() as session:
        author = session.scalar(select(Author).where(Author.id == data.id))
        
        upd = update(Author).where(Author.id == id).values(
            name=data.name,
            email=data.email, 
            password=data.password,
            bio=data.bio
        )
        session.execute(upd)
        return author