from fastapi import APIRouter

router = APIRouter()

@router.get("/tomorrow")
def get_tomorrow():
    return {"message": "hello tomorrow"}