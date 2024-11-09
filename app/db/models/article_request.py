from sqlmodel import SQLModel
from typing import List
from datetime import datetime
from pydantic import model_validator
from fastapi import HTTPException

from ...logging.logg import validations_logger

class DateRange(SQLModel):
    start_date:datetime
    end_date:datetime


    @model_validator(mode="after")
    def check_model(self):
        if self.start_date >= self.end_date:
            validations_logger.info("Model: DateRange, Field: start_date, Result: Failed (start date is not before end date)")
            raise HTTPException(status_code=400,detail="Start date should be before end date")
        if self.end_date >= datetime.now():
            validations_logger.info("Model: DateRange, Field: end_date, Result: Failed (end date in future)")
            raise HTTPException(status_code=400,detail="End date cannot be in future")
        validations_logger.info("Model: DateRange, Result: Success")    
        return self


class ArticleRequest(SQLModel):
    keywords:List[str]
    date_range:DateRange