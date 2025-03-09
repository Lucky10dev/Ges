# models/utente_model.py

from sqlalchemy import Column, Integer, String, Enum
from models.base_model import Base
from werkzeug.security import generate_password_hash, check_password_hash
import enum

class RuoloUtente(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'

class Utente(Base):
    __tablename__ = 'utenti'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

