from fastapi import FastAPI


from app.controllers.tomorrowController import tomorrowController
from app.controllers.forecastsController import forecastsController

app = FastAPI()

app.include_router(forecastsController.router)
app.include_router(tomorrowController.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
