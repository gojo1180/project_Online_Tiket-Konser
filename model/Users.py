from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from utils.DB import Base

class User(Base):
    __tablename__ = "User"

    User_Id = Column(Integer, primary_key=True, index=True)
    Username = Column(String(250), unique=True, index=True)
    Email = Column(String(250), unique=True, index=True)
    Password = Column(String(250))
    Status = Column(String(30), default="active")  # bisa "active" atau "inactive"
    histori_list = relationship("Histori", back_populates="user")