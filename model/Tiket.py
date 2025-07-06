from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from utils.DB import Base

class Tiket(Base):
    __tablename__ = 'Tiket'

    Id_Tiket = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Tiket = Column(String(150), nullable=False)
    Jenis_Tiket = Column(String(150), nullable=False)
    Stock = Column(Integer, nullable=False)
    Harga = Column(Integer, nullable=False)
    Days = Column(String(150), nullable=False)
    Detail = Column(Text, nullable=True)
    histori_list = relationship("Histori", back_populates="tiket")