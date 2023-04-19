from typing import List
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Person(BaseModel):
    id: int 
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Isabel", age=18),
    Person(id=2, name="Elijah", age= 24)
]


@app.get("/api")
def read_root():
    return DB