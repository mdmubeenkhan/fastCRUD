from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int
    ondiscount: Optional[bool] = False

    class Config:
        orm_mode = True
