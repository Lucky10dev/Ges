from views.main_view import MainView
from controllers.clienti_controller import ClientiController
from controllers.appuntamenti_controller import AppuntamentiController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.clienti_controller = ClientiController()
        self.appuntamenti_controller = AppuntamentiController()
        self.connect_signals()

    def connect_signals(self):
        self.view.btnClienti.clicked.connect(self.on_btnClienti_clicked)
        self.view.btnAgenda.clicked.connect(self.on_btnAgenda_clicked)

    def on_btnClienti_clicked(self):
        self.clienti_controller.show()

    def on_btnAgenda_clicked(self):
        self.appuntamenti_controller.show()

    def show(self):
        self.view.show()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show()
    sys.exit(app.exec_())