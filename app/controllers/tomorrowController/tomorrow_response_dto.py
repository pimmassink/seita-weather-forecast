from pydantic import BaseModel, Field

class TomorrowResponseDto(BaseModel):
    is_warm: bool = Field(alias="isWarm")
    is_sunny: bool = Field(alias="isSunny")
    is_windy: bool = Field(alias="isWindy")

    class Config:
        populate_by_name = True