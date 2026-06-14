from fastapi import FastAPI

from app.database.db import engine
from app.database.db import Base

from app.models.order import Order

from app.api.orders import router as order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Analytics Platform"
)

app.include_router(order_router)


@app.get("/")
def home():
    return {
        "message": "Analytics Platform Running"
    }
