# controllers/login_controller.py

from views.login_view import LoginView
from controllers.main_controller import MainController
from controllers.utente_controller import UtenteController
from PyQt5.QtWidgets import QMessageBox

class LoginController:
    def __init__(self):
        self.view = LoginView()
        self.utente_controller = UtenteController()
        self.view.btnLogin.clicked.connect(self.handle_login)
        self.main_controller = None

    def handle_login(self):
        username = self.view.lineEditUsername.text()
        password = self.view.lineEditPassword.text()

        if self.utente_controller.authenticate(username, password):
            QMessageBox.information(self.view, "Successo", "Accesso effettuato.")
            self.view.accept()
            self.main_controller = MainController()
            self.main_controller.show()
        else:
            QMessageBox.warning(self.view, "Errore", "Credenziali non valide.")

    def show(self):
        self.view.exec_()