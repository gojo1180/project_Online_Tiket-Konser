from pydantic import BaseModel

class HistoriSchema(BaseModel):
    email: str
    Id_Tiket: int
    jumlah: int
    total: int
    metode: str

# Untuk input ketika create histori
class HistoriCreate(BaseModel):
    email: str
    Id_Tiket: int
    jumlah: int
    total: int
    metode: str

# Untuk response/output data histori
class HistoriOut(BaseModel):
    Id_Histori: int
    Id_Tiket: int
    Id_User: int
    Jumlah_Tiket: int
    Total_Harga: int
    Pembayaran: str

    class Config:
        orm_mode = True