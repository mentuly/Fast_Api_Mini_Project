from fastapi import FastAPI
from .db import migrate
from .routes import (
    app,
    author_router,
    article_router,
    comment_router,
    request_router,
    auth_router,
)
