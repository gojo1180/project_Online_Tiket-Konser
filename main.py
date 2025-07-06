from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.DB import Base, engine
from routes import user_route
from routes import galeri_route
from routes import tiket_route
from routes import Histori_route

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user_route.router)
app.include_router(galeri_route.router)
app.include_router(tiket_route.router)
app.include_router(Histori_route.router)