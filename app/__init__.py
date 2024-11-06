from .db import migrate
from fastapi import FastAPI
from .routes import app,author_router,article_router,comment_router
