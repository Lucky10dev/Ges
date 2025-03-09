from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class ClientiView(QMainWindow):
    def __init__(self):
        super(ClientiView, self).__init__()
        loadUi('views/ui/clienti.ui', self)