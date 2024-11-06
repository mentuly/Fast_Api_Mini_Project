from fastapi import FastAPI


app = FastAPI()


from . import article,author,comment
from .article import article_router
from .comment import comment_router 
from .author import author_router