from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class ModClienteView(QDialog):
    def __init__(self):
        super(ModClienteView, self).__init__()
        loadUi('views/ui/mod_cliente.ui', self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)