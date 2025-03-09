# scripts/create_admin.py

import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.utente_controller import UtenteController

if __name__ == '__main__':
    username = input("Inserisci il nome utente dell'amministratore: ")
    password = input("Inserisci la password dell'amministratore: ")

    utente_controller = UtenteController()
    utente_controller.create_user(username, password)

    print("Utente amministratore creato con successo.")
