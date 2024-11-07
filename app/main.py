from fastapi import FastAPI

from app.controllers import forecastsController, tomorrowController

app = FastAPI()

app.include_router(forecastsController.router)
app.include_router(tomorrowController.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
