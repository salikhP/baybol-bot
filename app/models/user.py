from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # user telegram ID
    preferences = Column(JSONB)
