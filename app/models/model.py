from sqlalchemy import Boolean, Integer, String, Column, Float

from db.db import Base


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=True, default=0)
    ondiscount = Column(Boolean, default=False)
