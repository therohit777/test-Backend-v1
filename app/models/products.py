from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    name: str
    creationTime: datetime
    cost: float
    inputTask: List[str] = ["Default Task"]
    outputTask: List[str] = []
    deploymentStatus: bool = False
