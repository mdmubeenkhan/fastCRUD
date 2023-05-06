from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import Depends, HTTPException, status, APIRouter
from db.db import get_db
from models import model
from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from schemas import schema
import json


router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.post("/")
def add_new_product(payload: schema.Product, db: Session = Depends(get_db)):
    new_product = model.Products(**payload.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"data": new_product}


# skip is used by frontend for pagination
@router.get("/get-detailed")
def get_query_param(db: Session = Depends(get_db), limit: int = 5, skip=0,
                    search: Optional[str] = ""):
    data = db.query(model.Products).filter(
        model.Products.name.contains(search)).limit(limit).offset(skip).all()
    return data
