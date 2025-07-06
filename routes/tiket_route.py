from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.DB import get_db
from schema.TiketSchema import TiketCreate, TiketOut,TiketUpdate
from controler import TiketController
from controler.TiketController import get_one_tiket_per_day

router = APIRouter()

@router.get("/api/Get_tiket", response_model=list[TiketOut])
def get_tikets(db: Session = Depends(get_db)):
    return TiketController.get_all_tiket(db)

@router.get("/api/tiket_per_day", response_model=list[TiketOut])
def read_tiket_per_day(db: Session = Depends(get_db)):
    return get_one_tiket_per_day(db)

@router.get("/api/tiket/{id_tiket}", response_model=TiketOut)
def get_tiket_by_id(id_tiket: int, db: Session = Depends(get_db)):
    tiket = TiketController.get_tiket_by_id(db, id_tiket)
    if not tiket:
        raise HTTPException(status_code=404, detail="Tiket tidak ditemukan")
    return tiket

@router.post("/api/Create_tiket", response_model=TiketOut)
def create_tiket(tiket: TiketCreate, db: Session = Depends(get_db)):
    return TiketController.create_tiket(db, tiket)

@router.put("/api/Update_tiket/{tiket_id}", response_model=TiketOut)
def update_tiket(tiket_id: int, tiket: TiketUpdate, db: Session = Depends(get_db)):
    result = TiketController.update_tiket(db, tiket_id, tiket)
    if not result:
        raise HTTPException(status_code=404, detail="Tiket tidak ditemukan")
    return result

@router.delete("/api/Delete_tiket/{tiket_id}")
def delete_tiket(tiket_id: int, db: Session = Depends(get_db)):
    result = TiketController.delete_tiket(db, tiket_id)
    if not result:
        raise HTTPException(status_code=404, detail="Tiket tidak ditemukan")
    return {"message": "Tiket berhasil dihapus"}
