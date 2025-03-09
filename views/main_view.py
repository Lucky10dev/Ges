from PyQt5.QtWidgets import QMainWindow
from views.ui.dashboard_ui import Ui_MainWindow
import views.resources_rc  # Importa il file delle risorse generato

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)

    def on_btnAgenda_clicked(self):
        print("Agenda button clicked")
        # Implementa la logica per aprire la vista degli appuntamenti

    def on_btnClienti_clicked(self):
        print("Clienti button clicked")
        # Implementa la logica per aprire la vista dei clienti