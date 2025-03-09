# database/create_db.py

import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import Base
from database.setup import engine
import models.utente_model
import models.clienti_model
import models.appuntamenti_model
# Importa altri modelli se necessari

Base.metadata.create_all(engine)
