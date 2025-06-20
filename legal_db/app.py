from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Madagascar Legal DB")

class Law(BaseModel):
    id: int
    title: str
    content: str

# In-memory store as placeholder
laws_db: List[Law] = [
    Law(id=1, title="Sample Law", content="Full text of law"),
]

@app.get("/laws", response_model=List[Law])
def list_laws():
    """Return available laws"""
    return laws_db

@app.get("/laws/{law_id}", response_model=Law)
def get_law(law_id: int):
    for law in laws_db:
        if law.id == law_id:
            return law
    return {"error": "Law not found"}
