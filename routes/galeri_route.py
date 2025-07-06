from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from utils.DB import get_db
from controler.GaleriController import create_galeri, get_all_galeri, update_galeri_controller, delete_galeri_controller

router = APIRouter()

@router.post("/api/galeri")
def upload_galeri(
    nama_artis: str = Form(...),
    detail: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return create_galeri(db=db, nama_artis=nama_artis, detail=detail, image=image)

@router.get("/api/Get_galeri")
def read_all_galeri(db: Session = Depends(get_db)):
    return get_all_galeri(db)

@router.put("/api/Update_galeri/{galeri_id}")
def update_galeri(galeri_id: int, nama_artis: str = Form(...), detail: str = Form(...), image: UploadFile = File(None), db: Session = Depends(get_db)):
    return update_galeri_controller(db, galeri_id, nama_artis, detail, image)

@router.delete("/api/Delete_galeri/{galeri_id}")
def delete_galeri(galeri_id: int, db: Session = Depends(get_db)):
    return delete_galeri_controller(db, galeri_id)
