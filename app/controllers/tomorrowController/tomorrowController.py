from datetime import datetime

from fastapi import APIRouter

from app.controllers.tomorrowController.tomorrow_response_dto import TomorrowResponseDto

router = APIRouter()

@router.get("/tomorrow")
def get_tomorrow(now: datetime):
    response = TomorrowResponseDto(is_warm=True, is_sunny=False, is_windy=True)
    return response