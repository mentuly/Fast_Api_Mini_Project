from sqlmodel import Field,SQLModel
from datetime import datetime

class PUBMixin(SQLModel):
    published_at:str = Field(default=datetime.now())