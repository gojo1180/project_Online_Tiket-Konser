from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.DB import get_db
from schema.HistoriShema import HistoriCreate
from controler.HistoriController import create_histori,get_histori_by_email

router = APIRouter()

@router.post("/api/save-histori")
def save_histori(data: HistoriCreate, db: Session = Depends(get_db)):
    return create_histori(data, db)

@router.get("/api/histori/user/{email}")
def get_user_histori(email: str, db: Session = Depends(get_db)):
    return get_histori_by_email(email, db)