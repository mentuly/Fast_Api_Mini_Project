from sqlmodel import SQLModel
from typing import List
from datetime import datetime
from pydantic import model_validator
from fastapi import HTTPException

class DateRange(SQLModel):
    start_date:datetime
    end_date:datetime


    @model_validator(mode="after")
    def check_model(self):
        if self.start_date >= self.end_date:
            raise HTTPException(status_code=400,detail="Start date should be before end date")
        if self.end_date >= datetime.now():
            raise HTTPException(status_code=400,detail="End date cannot be in future")
        return self


class ArticleRequest(DateRange):
    keywords:List[str]
    