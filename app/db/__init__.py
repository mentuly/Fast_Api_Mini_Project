from .models import Config, Comment, Article, ArticleRequest, Author, Token


def up():
    Config.BASE.metadata.create_all(Config.ENGINE)


def down():
    Config.BASE.metadata.drop_all(Config.ENGINE)


def migrate():
    down()
    up()


def down():
    Config.BASE.metadata.drop_all(Config.ENGINE)


def migrate():
    down()
    up()
