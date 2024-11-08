from sqlmodel import Field,SQLModel
from datetime import datetime
from pydantic import model_validator
from fastapi import HTTPException
from typing import Optional

class PUBMixin(SQLModel):
    published_at:str = Field(default=datetime.now())

    
    @model_validator(mode="after")
    def check_date(self):
        fixed_date=datetime.strptime(self.published_at,"%Y-%m-%dT%H:%M:%S")
        if fixed_date >= datetime.now():
            raise HTTPException(status_code=400,detail="Date cannot be in future")
        return self