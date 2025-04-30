from pydantic import BaseModel

class TravelDetails(BaseModel):
    origin: str
    destination: str
    start_date: str
    end_date: str
    budget_amt: float
    budget_ccy: str