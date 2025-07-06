from pydantic import BaseModel

class GaleriBase(BaseModel):
    nama_artis: str
    detail: str

class GaleriResponse(GaleriBase):
    id: int

    class Config:
        orm_mode = True
