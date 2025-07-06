from sqlalchemy.orm import Session
from model.Tiket import Tiket
from sqlalchemy.sql import func
from schema.TiketSchema import TiketCreate,TiketUpdate

def get_all_tiket(db: Session):
    return db.query(Tiket).all()

def get_one_tiket_per_day(db: Session):
    subquery = (
        db.query(
            Tiket.Days,
            func.min(Tiket.Id_Tiket).label("min_id")
        )
        .group_by(Tiket.Days)
        .subquery()
    )

    result = db.query(Tiket).join(
        subquery, Tiket.Id_Tiket == subquery.c.min_id
    ).all()

    return result

def get_tiket_by_id(db: Session, tiket_id: int):
    return db.query(Tiket).filter(Tiket.Id_Tiket == tiket_id).first()

def create_tiket(db: Session, tiket_data: TiketCreate):
    new_tiket = Tiket(**tiket_data.dict())
    db.add(new_tiket)
    db.commit()
    db.refresh(new_tiket)
    return new_tiket

def update_tiket(db: Session, tiket_id: int, tiket_data: TiketUpdate):
    tiket = db.query(Tiket).filter(Tiket.Id_Tiket == tiket_id).first()
    if not tiket:
        return None
    for key, value in tiket_data.dict().items():
        setattr(tiket, key, value)
    db.commit()
    db.refresh(tiket)
    return tiket

def delete_tiket(db: Session, tiket_id: int):
    tiket = db.query(Tiket).filter(Tiket.Id_Tiket == tiket_id).first()
    if not tiket:
        return None
    db.delete(tiket)
    db.commit()
    return tiket
