# database/setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configura il motore del database (modifica la stringa di connessione secondo le tue esigenze)
engine = create_engine('sqlite:///c:/Users/solar/Desktop/GestionAle1/Gest/database/gestionale1.db')

# Crea una sessione
Session = sessionmaker(bind=engine)
session = Session()