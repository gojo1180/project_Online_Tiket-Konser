from fastapi import HTTPException
from model.Users import User
from model.Histori import Histori
from sqlalchemy.orm import Session
from utils.DB import get_db
from sqlalchemy.future import select
from model.Tiket import Tiket
from schema.HistoriShema import HistoriCreate


def create_histori(data: HistoriCreate, db: Session):
    user = db.query(User).filter(User.Email == data.email).first()
    tiket = db.query(Tiket).filter(Tiket.Id_Tiket == data.Id_Tiket).first()

    if not user or not tiket:
        raise HTTPException(status_code=404, detail="User atau Tiket tidak ditemukan")

    if tiket.Stock < data.jumlah:
        raise HTTPException(status_code=400, detail="Stok tiket tidak mencukupi")

    # Kurangi stok tiket
    tiket.Stock -= data.jumlah

    # Simpan histori
    histori = Histori(
        Id_Tiket=data.Id_Tiket,
        Id_User=user.User_Id,
        Jumlah_Tiket=data.jumlah,
        Total_Harga=data.total,
        Pembayaran=data.metode
    )

    db.add(histori)
    db.commit()
    db.refresh(histori)

    return {"message": "Histori berhasil disimpan dan stok diperbarui"}


def get_histori_by_email(email: str, db: Session):
    user = db.query(User).filter(User.Email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    histori_list = db.query(Histori).filter(Histori.Id_User == user.User_Id).all()

    result = []
    for h in histori_list:
        tiket = db.query(Tiket).filter(Tiket.Id_Tiket == h.Id_Tiket).first()
        result.append({
            
            "Jenis_Tiket": tiket.Jenis_Tiket if tiket else "Tiket tidak ditemukan",
            "Days": tiket.Days if tiket else None,
            "Jumlah_Tiket": h.Jumlah_Tiket,
            "Total_Harga": h.Total_Harga,
            "Pembayaran": h.Pembayaran
        })

    return result

