from fastapi import APIRouter
from sqlalchemy import func

from app.database.db import SessionLocal
from app.models.order import Order

router = APIRouter()


@router.post("/orders")
def create_order():

    db = SessionLocal()

    order = Order(
        customer_name="Rahul",
        product_name="Laptop",
        amount=50000
    )

    db.add(order)
    db.commit()
    db.close()

    return {"message": "Order inserted successfully"}


@router.get("/orders")
def get_orders():

    db = SessionLocal()

    orders = db.query(Order).all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "customer_name": order.customer_name,
            "product_name": order.product_name,
            "amount": order.amount
        })

    db.close()

    return result


@router.get("/analytics/kpi")
def get_kpi():

    db = SessionLocal()

    total_orders = db.query(Order).count()

    total_revenue = db.query(
        func.sum(Order.amount)
    ).scalar()

    db.close()

    return {
        "total_orders": total_orders,
        "total_revenue": total_revenue
    }


@router.get("/analytics/top-customers")
def top_customers():

    db = SessionLocal()

    data = (
        db.query(
            Order.customer_name,
            func.sum(Order.amount).label("revenue")
        )
        .group_by(Order.customer_name)
        .order_by(func.sum(Order.amount).desc())
        .all()
    )

    db.close()

    return [
        {
            "customer_name": row[0],
            "revenue": row[1]
        }
        for row in data
    ]
