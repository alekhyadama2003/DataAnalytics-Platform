from sqlalchemy import Column, Integer, Float, String

from app.database.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String, nullable=False)

    product_name = Column(String, nullable=False)

    amount = Column(Float, nullable=False)
