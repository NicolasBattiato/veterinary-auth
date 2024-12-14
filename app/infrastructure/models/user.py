from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.infrastructure.models.base import BaseModel
from datetime import datetime

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    type_user = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)

    def to_access_token(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "user_id": self.id,
            "is_active": self.is_active
        }