# scripts/init_db.py

import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.clienti_model import Cliente, SchedaCliente, ImmagineScheda

def init_db():
    # Configura il motore del database (modifica la stringa di connessione secondo le tue esigenze)
    engine = create_engine('sqlite:///c:/Users/solar/Desktop/GestionAle1/Gest/database/gestionale1.db')
    
    # Crea tutte le tabelle
    Base.metadata.create_all(engine)
    print("Database inizializzato con successo.")

if __name__ == '__main__':
    init_db()