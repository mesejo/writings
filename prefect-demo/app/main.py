from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Company(BaseModel):
    company_id: str
    segment: str


@app.put("/companies/")
async def update_companies(companies: List[Company]):
    for company in companies:
        # Do something with the company
        print(company.company_id, company.segment)
    return {"message": "Companies updated successfully"}
