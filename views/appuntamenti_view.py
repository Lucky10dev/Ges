from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class AppuntamentiView(QMainWindow):
    def __init__(self):
        super(AppuntamentiView, self).__init__()
        loadUi('views/ui/appuntamenti.ui', self)
