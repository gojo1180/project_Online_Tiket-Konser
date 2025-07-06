from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils.DB import Base

class Histori(Base):
    __tablename__ = "Histori"

    Id_Histori = Column(Integer, primary_key=True, autoincrement=True)
    Id_Tiket = Column(Integer, ForeignKey("Tiket.Id_Tiket"), nullable=False)
    Id_User = Column(Integer, ForeignKey("User.User_Id"), nullable=False)
    Jumlah_Tiket = Column(Integer, nullable=False)
    Total_Harga = Column(Integer, nullable=False)
    Pembayaran = Column(String(150), nullable=False)
    tiket = relationship("Tiket", back_populates="histori_list")
    user = relationship("User", back_populates="histori_list")
