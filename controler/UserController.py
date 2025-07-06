from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, Cookie
from fastapi import HTTPException
from model.Users import User
from schema.UserSchema import UserCreate
from schema.UserSchema import UserCreate, UserLogin, UserResponse, UserUpdate
import hashlib
import uuid

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(db: Session, user: UserCreate):
    # Periksa apakah email sudah terdaftar
    if db.query(User).filter(User.Email == user.email).first():
        return {"success": False, "message": "Email sudah terdaftar."}

    # Membuat user baru
    new_user = User(
        Username=user.username,
        Email=user.email,
        Password=hash_password(user.password),
        Status=user.status  # Menyertakan status sesuai input atau default 'active'
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Menyegarkan data user yang baru ditambahkan
    return {"success": True, "message": "Registrasi berhasil."}

def login_user(db: Session, credentials: UserLogin, response: Response = None):
    user = db.query(User).filter(User.Email == credentials.email).first()

    if not user or user.Password != hash_password(credentials.password):
        raise HTTPException(status_code=401, detail="Email atau password salah")
    
    if user.Status == "nonactive":
        raise HTTPException(status_code=403, detail="Akun Anda sudah tidak aktif")

    return {
        "message": "Login berhasil",
        "username": user.Username,
        "email": user.Email,
        "is_admin": user.Status == "admin"  # Misalnya field 'Status' menyimpan 'admin'
    }


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.Email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return {
        "username": user.Username,
        "email": user.Email,
        "status": user.Status
    }

def update_user(db: Session, update_data: UserUpdate):
    user = db.query(User).filter(User.Email == update_data.old_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    if update_data.password:
        user.Password = hash_password(update_data.password)

    user.Email = update_data.email
    user.Username = update_data.username
    db.commit()
    db.refresh(user)

    return {"success": True, "message": "User berhasil diupdate"}

def delete_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.Email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    user.Status = "nonactive"  # Update status, tidak menghapus permanen
    db.commit()
    return {"success": True, "message": "Akun telah dinonaktifkan"}


def get_all_users(db: Session):
    return [
        {"email": user.Email, "username": user.Username, "status": user.Status}
        for user in db.query(User).all()
    ]

def promote_user_to_admin(db: Session, email: str):
    user = db.query(User).filter(User.Email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    user.Status = "admin"
    db.commit()
    return {"message": f"{user.Email} sekarang menjadi admin"}

def demote_user_to_active(db: Session, email: str):
    user = db.query(User).filter(User.Email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    user.Status = "active"
    db.commit()
    return {"message": f"{user.Email} telah dikembalikan ke status aktif"}
