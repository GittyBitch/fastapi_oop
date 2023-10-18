from pydantic import BaseModel
from typing import Optional

class StudentModel(BaseModel):
        id: str
        name: str
        sex: str
        castrated: str
        stars:str


