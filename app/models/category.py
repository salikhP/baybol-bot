from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from app.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    category_name=Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
