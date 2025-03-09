# models/appuntamenti_model.py

from sqlalchemy import Column, Integer, Date, Time, String
from models.base_model import Base

class Appuntamento(Base):
    __tablename__ = 'appuntamenti'
    
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    ora = Column(Time, nullable=False)
    durata = Column(Integer, nullable=False)
    trattamento = Column(String, nullable=False)
    note = Column(String)
