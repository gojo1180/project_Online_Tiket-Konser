from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, Depends, Response
from schema.UserSchema import UserCreate
from controler.UserController import register_user, get_user_by_email
from schema.UserSchema import UserCreate, UserLogin
from utils.DB import get_db
from sqlalchemy.orm import Session
from schema.UserSchema import UserLogin,PromoteRequest
from controler.UserController import login_user,update_user, get_all_users,promote_user_to_admin, demote_user_to_active, delete_user_by_email
from fastapi import APIRouter
from schema.UserSchema import UserResponse,UserUpdate


router = APIRouter(
    prefix="/api",
    tags=["User"]
)
session_store = {}

@router.post("/register")
async def api_register(user: UserCreate, db: Session = Depends(get_db)):
    result = register_user(db, user)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": result["message"]}

@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, credentials)

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("session_token")
    return {"success": True, "message": "Logout berhasil"}

@router.get("/user/{email}", response_model=UserResponse)
def get_user(email: str, db: Session = Depends(get_db)):
    return get_user_by_email(db, email)

@router.put("/user/update")
def update_user_data(update_data: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, update_data)

@router.delete("/user/delete/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    return delete_user_by_email(email, db)


# Endpoint ambil semua user
@router.get("/users")
def fetch_users(db: Session = Depends(get_db)):
    return get_all_users(db)

# Endpoint ubah status user menjadi admin
@router.put("/user/promote")
def promote_user(request: PromoteRequest, db: Session = Depends(get_db)):
    return promote_user_to_admin(db, request.email)


@router.put("/user/demote")
def demote_user(request: PromoteRequest, db: Session = Depends(get_db)):
    return demote_user_to_active(db, request.email)
