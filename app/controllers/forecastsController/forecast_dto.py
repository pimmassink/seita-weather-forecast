from datetime import datetime

from pydantic import BaseModel


# TODO Pim, I have no idea what this will look like. I should design this later.
class ForecastDto(BaseModel):
    date: datetime
    temperature: float
    weather: str
