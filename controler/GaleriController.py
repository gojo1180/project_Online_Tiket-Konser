from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from model.Galeri import Galeri
import base64
def create_galeri(db: Session, nama_artis: str, detail: str, image: UploadFile):
    try:
        image_data = image.file.read()
    except Exception:
        raise HTTPException(status_code=400, detail="Gagal membaca file")

    galeri = Galeri(
        Nama_Artis=nama_artis,
        Detail=detail,
        Image=image_data
    )

    db.add(galeri)
    db.commit()
    db.refresh(galeri)
    return {"message": "Galeri berhasil ditambahkan", "data": galeri.Id}

def get_all_galeri(db: Session):
    galeris = db.query(Galeri).all()
    result = []
    for g in galeris:
        result.append({
            "id": g.Id,
            "nama_artis": g.Nama_Artis,
            "detail": g.Detail,
            "image": base64.b64encode(g.Image).decode("utf-8")  # Convert BLOB to base64
        })
    return result

def update_galeri_controller(db: Session, galeri_id: int, nama_artis: str, detail: str, image: UploadFile = None):
    galeri = db.query(Galeri).filter(Galeri.Id == galeri_id).first()
    if not galeri:
        raise HTTPException(status_code=404, detail="Galeri tidak ditemukan")
    
    galeri.Nama_Artis = nama_artis
    galeri.Detail = detail
    if image:
        galeri.Image = image.file.read()

    db.commit()
    return {"message": "Galeri berhasil diperbarui"}

def delete_galeri_controller(db: Session, galeri_id: int):
    galeri = db.query(Galeri).filter(Galeri.Id == galeri_id).first()
    if not galeri:
        raise HTTPException(status_code=404, detail="Galeri tidak ditemukan")
    
    db.delete(galeri)
    db.commit()
    return {"message": "Galeri berhasil dihapus"}

