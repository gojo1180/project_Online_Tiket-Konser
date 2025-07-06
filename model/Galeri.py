from sqlalchemy import Column, Integer, String, LargeBinary, Text
from utils.DB import Base  # pastikan Base diambil dari deklarasi database kamu

class Galeri(Base):
    __tablename__ = "Galeri"

    Id = Column(Integer, primary_key=True, index=True)
    Image = Column(LargeBinary(length=(2**32)-1), nullable=False)
    Nama_Artis = Column(String(100), nullable=False)
    Detail = Column(Text, nullable=True)
 