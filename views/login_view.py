# views/login_view.py

from PyQt5 import QtWidgets, uic
import os

class LoginView(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join('views', 'ui', 'login.ui'), self)
