from pydantic import BaseModel, Field

class GetFlightInPeriodCheckInput(BaseModel):
    fly_from: str = Field(
        None,
        description="the 3-digit IATA code for departure airport"
    )
    fly_to: str = Field(
        None,
        description="the 3-digit IATA code for arrival airport"
    )
    date_from: str = Field(
        None,
        description="the dd/mm/yyyy format of start date for the range of search"
    )
    date_to: str = Field(
        None,
        description="the dd/mm/yyyy format of end date for the range of search"
    )
    sort: str = Field(
        None,
        description="the category for low-to-high sorting, only support 'price', 'duration', 'date'"
    )

class RequestBody(BaseModel):
    input: str
    firstMsg: bool