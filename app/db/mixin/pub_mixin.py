from sqlmodel import Field,SQLModel
from datetime import datetime

class PUBMixin(SQLModel):
    published_at:datetime = Field(default=datetime.now())