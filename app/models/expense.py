from sqlalchemy import Column, Integer, Float, String, Date, DateTime, ForeignKey, func
from app.db import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    item_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    note = Column(String, nullable=True)
    raw_text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())