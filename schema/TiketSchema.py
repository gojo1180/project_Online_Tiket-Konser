from pydantic import BaseModel
from typing import Optional

class TiketBase(BaseModel):
    Tiket: str
    Jenis_Tiket: str
    Stock: int
    Harga: int
    Days: str
    Detail: Optional[str] = None

class TiketCreate(TiketBase):
    pass

class TiketUpdate(TiketBase):
    pass

class TiketOut(TiketBase):
    Id_Tiket: int

    class Config:
        orm_mode = True
