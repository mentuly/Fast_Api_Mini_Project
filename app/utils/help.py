from ..db import Config



def get_session():
    with Config.SESSION.begin() as session:
        yield session