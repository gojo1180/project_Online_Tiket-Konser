from pydantic import BaseModel, EmailStr
from typing import List, Optional
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    status: str = "active"  # status default adalah 'active'

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: str

class UserUpdate(BaseModel):
    old_email: EmailStr   # ← Tambahkan ini
    email: EmailStr
    username: str
    old_password: str
    password: Optional[str] = None


class PromoteRequest(BaseModel):
    email: EmailStr
    
    class Config:
        orm_mode = True  # Agar bisa dikonversi menjadi objek SQLAlchemy
