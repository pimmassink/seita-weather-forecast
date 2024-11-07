from fastapi import APIRouter

router = APIRouter()

@router.get("/forecasts")
def get_forecasts():
    return {"message": "hello forecasts"}