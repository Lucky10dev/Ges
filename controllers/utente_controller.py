# controllers/utente_controller.py

import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.utente_model import Utente
from models.base_model import Base
from werkzeug.security import generate_password_hash, check_password_hash

class UtenteController:
    def __init__(self):
        # Configura il motore del database (modifica la stringa di connessione secondo le tue esigenze)
        self.engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def create_user(self, username, password):
        # Verifica se l'utente esiste già
        if self.session.query(Utente).filter_by(username=username).first():
            print(f"Utente {username} esiste già.")
            return

        # Crea un nuovo utente
        password_hash = generate_password_hash(password)
        new_user = Utente(username=username, password_hash=password_hash)
        self.session.add(new_user)
        self.session.commit()
        print(f"Utente {username} creato con successo.")

    def authenticate(self, username, password):
        # Autentica l'utente
        user = self.session.query(Utente).filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return True
        return False


