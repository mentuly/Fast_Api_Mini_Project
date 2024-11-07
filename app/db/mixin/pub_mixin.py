from sqlmodel import Field,SQLModel
from datetime import datetime
from pydantic import model_validator
from fastapi import HTTPException

class PUBMixin(SQLModel):
    published_at:str = Field(default=datetime.now())

    
    @model_validator(mode="after")
    def check_date(self):
        if self.published_at >= datetime.now():
            raise HTTPException(status_code=400,detail="Date cannot be in future")
        return self