from PyQt5.QtWidgets import QDialog, QFileDialog, QListWidgetItem, QGraphicsScene
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap

class SchedaClienteView(QDialog):
    def __init__(self):
        super(SchedaClienteView, self).__init__()
        loadUi('views/ui/scheda_cliente.ui', self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.btnAddImage.clicked.connect(self.add_image)
        self.listWidgetImages.itemClicked.connect(self.display_image)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def add_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleziona Immagine", "", "Immagini (*.png *.jpg *.jpeg *.bmp);;Tutti i file (*)", options=options)
        if file_name:
            item = QListWidgetItem(file_name)
            self.listWidgetImages.addItem(item)

    def display_image(self, item):
        pixmap = QPixmap(item.text())
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.graphicsView.fitInView(self.scene.itemsBoundingRect(), 1)

    def clear_graphics_view(self):
        self.scene.clear()