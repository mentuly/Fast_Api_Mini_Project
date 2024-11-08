from ..db import Author
from sqlmodel import select, update,Session
from fastapi import APIRouter,HTTPException,Depends
from ..utils import get_session
from typing import Annotated

author_router =APIRouter(prefix="/author", tags=["Author"])




@author_router.get("/all")
def all_authors(session:Annotated[Session,Depends(get_session)]):
    resp=[]
    authors = session.scalars(select(Author)).all()
    for author in authors:
        resp.append(author)
    return resp

@author_router.post("/create")
def create_author(data:Author,session:Annotated[Session,Depends(get_session)]):
    author = Author(**data.model_dump())
    session.add(author)
    return "Created"

@author_router.delete("/delete/{id}")
def del_author(id:int,session:Annotated[Session,Depends(get_session)]):
    
    author = session.scalar(select(Author).where(Author.id==id))
    if not author:
        raise HTTPException(status_code=404,detail="No author with this id")
    session.delete(author)
    return "Deleted"


@author_router.delete("/delete_all")
def del_all_authors(session:Annotated[Session,Depends(get_session)]):
    authors = session.scalars(select(Author)).all()
    for author in authors:
        session.delete(author)
        return "Deleted"
    

@author_router.get("/{id}")
def one_author(id:int,session:Annotated[Session,Depends(get_session)]):
    author=session.scalar(select(Author).where(Author.id==id))
    if not author:
        raise HTTPException(status_code=404,detail="No author with this id")
    return author

@author_router.put("/{id}")
def update_author(id:int,data: Author,session:Annotated[Session,Depends(get_session)]):
    author = session.scalar(select(Author).where(Author.id == id))
    if not author:
        raise HTTPException(status_code=404,detail="No author with this id")
    upd = update(Author).where(Author.id == id).values(**data.model_dump())
    
    session.execute(upd)
    return author