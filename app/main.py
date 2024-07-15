# FastAPI crud app

from fastapi import FastAPI
from app.models import model
from app.db.db import engine
from app.routers import product


from fastapi.middleware.cors import CORSMiddleware
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://www.google.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product.router)
