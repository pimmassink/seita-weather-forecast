from datetime import datetime

from fastapi import APIRouter

from app.controllers.forecastsController.forecast_dto import ForecastDto

router = APIRouter()

@router.get("/forecasts")
def get_forecasts(now: datetime, then: datetime):
    response: list[ForecastDto] = [
        ForecastDto(date=now, temperature=10.0, weather="sunny"),
        ForecastDto(date=then, temperature=15.0, weather="cloudy"),
    ]
    return response