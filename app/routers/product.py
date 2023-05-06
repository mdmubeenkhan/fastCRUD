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


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    data = db.query(model.Products).all()
    return {"data": data}
