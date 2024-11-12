from datetime import datetime
from sqlmodel import Field, SQLModel
from pydantic import model_validator
from fastapi import HTTPException

from ...logging.logg import validations_logger


class PUBMixin(SQLModel):
    published_at: str = Field(default=datetime.now())

    @model_validator(mode="after")
    def check_date(self):
        fixed_date = datetime.strptime(self.published_at, "%Y-%m-%dT%H:%M:%S")
        if fixed_date >= datetime.now():
            validations_logger.info(
                "Model: PUBMixin, Field: published_at, Result: Failed (date in future)"
            )
            raise HTTPException(status_code=400, detail="Date cannot be in future")
        validations_logger.info("Model: PUBMixin, Field: published_at, Result: Success")
        return self
