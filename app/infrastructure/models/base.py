import uuid
import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import as_declarative


def generate_uuid():
    return str(uuid.uuid4())

@as_declarative()
class Base:
    pass  

class BaseModel(Base):
    """Base DB Model with shared attributes."""

    __abstract__ = True  

    id = Column(String(36), primary_key=True, default=generate_uuid) 
    created_at = Column(DateTime, default=datetime.datetime.now) 
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)  
    deleted_at = Column(DateTime, default=None)  

    def to_dict(self):
        """Convierte el objeto en un diccionario."""
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at
        }
