from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    type_user: str
    is_active: bool = False  
    created_at: datetime  
    updated_at: datetime  
    deleted_at: Optional[datetime] = None 

class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    type_user: str

    is_active: bool = False  
    created_at: datetime  
    updated_at: datetime  
    deleted_at: Optional[datetime] = None 
    
    class Config:
        orm_mode = True


