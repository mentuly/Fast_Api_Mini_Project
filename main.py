import uvicorn
from app import app, migrate,author_router,article_router,comment_router

if __name__ == "__main__":
    migrate()
    app.include_router(author_router)
    app.include_router(article_router)
    app.include_router(comment_router)
    uvicorn.run(app,port=8080)