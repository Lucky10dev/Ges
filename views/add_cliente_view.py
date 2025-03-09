from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class AddClienteView(QDialog):
    def __init__(self):
        super(AddClienteView, self).__init__()
        loadUi('views/ui/add_cliente.ui', self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)