from datetime import datetime

from fastapi import APIRouter

from app.controllers.forecastsController.forecast_response_dto import ForecastResponseDto

router = APIRouter()

@router.get("/forecasts")
def get_forecasts(now: datetime, then: datetime):
    response: list[ForecastResponseDto] = [
        ForecastResponseDto(date=now, temperature=10.0, weather="sunny"),
        ForecastResponseDto(date=then, temperature=15.0, weather="cloudy"),
    ]
    return response