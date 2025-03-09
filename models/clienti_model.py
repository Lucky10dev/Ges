from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base_model import Base

class Cliente(Base):
    __tablename__ = 'clienti'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)
    scheda = relationship("SchedaCliente", uselist=False, back_populates="cliente")

class SchedaCliente(Base):
    __tablename__ = 'schede_clienti'
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('clienti.id'))
    descrizione = Column(Text, nullable=True)
    cliente = relationship("Cliente", back_populates="scheda")
    immagini = relationship("ImmagineScheda", back_populates="scheda")

class ImmagineScheda(Base):
    __tablename__ = 'immagini_schede'
    id = Column(Integer, primary_key=True)
    id_scheda = Column(Integer, ForeignKey('schede_clienti.id'))
    percorso = Column(String, nullable=False)
    scheda = relationship("SchedaCliente", back_populates="immagini")