from views.clienti_view import ClientiView
from views.add_cliente_view import AddClienteView
from views.mod_cliente_view import ModClienteView
from views.scheda_cliente_view import SchedaClienteView
from models.clienti_model import Cliente, SchedaCliente, ImmagineScheda
from database.setup import session
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

class ClientiController:
    def __init__(self):
        self.view = ClientiView()
        self.add_cliente_view = AddClienteView()
        self.mod_cliente_view = ModClienteView()
        self.scheda_cliente_view = SchedaClienteView()
        self.current_scheda = None
        self.load_data()
        self.connect_signals()

    def load_data(self):
        clienti = session.query(Cliente).all()
        self.view.tableClienti.setRowCount(0)
        for row_number, cliente in enumerate(clienti):
            self.view.tableClienti.insertRow(row_number)
            self.view.tableClienti.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(cliente.id)))
            self.view.tableClienti.setItem(row_number, 1, QtWidgets.QTableWidgetItem(cliente.nome))
            self.view.tableClienti.setItem(row_number, 2, QtWidgets.QTableWidgetItem(cliente.cognome))
            self.view.tableClienti.setItem(row_number, 3, QtWidgets.QTableWidgetItem(cliente.telefono))
            self.view.tableClienti.setItem(row_number, 4, QtWidgets.QTableWidgetItem(cliente.email))
            btn_scheda = QtWidgets.QPushButton("Visualizza Scheda")
            btn_scheda.clicked.connect(lambda _, id_cliente=cliente.id: self.show_scheda_cliente(id_cliente))
            self.view.tableClienti.setCellWidget(row_number, 5, btn_scheda)

        # Imposta la dimensione predefinita delle sezioni dell'intestazione orizzontale
        self.view.tableClienti.horizontalHeader().setDefaultSectionSize(200)
        self.view.tableClienti.horizontalHeader().setStretchLastSection(True)

    def connect_signals(self):
        self.view.btnAddCliente.clicked.connect(self.show_add_cliente_dialog)
        self.add_cliente_view.buttonBox.accepted.connect(self.add_cliente)
        self.add_cliente_view.buttonBox.rejected.connect(self.cancel_add_cliente)
        self.view.btnEditCliente.clicked.connect(self.show_mod_cliente_dialog)
        self.mod_cliente_view.buttonBox.accepted.connect(self.edit_cliente)
        self.mod_cliente_view.buttonBox.rejected.connect(self.cancel_mod_cliente)
        self.view.btnDeleteCliente.clicked.connect(self.delete_cliente)
        self.view.btnFileCliente.clicked.connect(self.show_scheda_cliente_dialog)
        self.scheda_cliente_view.buttonBox.accepted.connect(self.add_scheda_cliente)
        self.scheda_cliente_view.buttonBox.rejected.connect(self.cancel_scheda_cliente)

    def show_add_cliente_dialog(self):
        self.add_cliente_view.lineEdit.clear()
        self.add_cliente_view.lineEdit_2.clear()
        self.add_cliente_view.lineEdit_3.clear()
        self.add_cliente_view.lineEdit_4.clear()
        self.add_cliente_view.exec_()

    def add_cliente(self):
        nome = self.add_cliente_view.lineEdit.text()
        cognome = self.add_cliente_view.lineEdit_2.text()
        telefono = self.add_cliente_view.lineEdit_3.text()
        email = self.add_cliente_view.lineEdit_4.text()

        nuovo_cliente = Cliente(
            nome=nome,
            cognome=cognome,
            telefono=telefono,
            email=email
        )
        session.add(nuovo_cliente)
        session.commit()

        self.load_data()
        QtWidgets.QMessageBox.information(self.add_cliente_view, "Successo", "Cliente aggiunto con successo.")
        self.add_cliente_view.accept()

    def cancel_add_cliente(self):
        self.add_cliente_view.reject()

    def show_mod_cliente_dialog(self):
        selected_row = self.view.tableClienti.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un cliente da modificare.")
            return

        id_cliente = int(self.view.tableClienti.item(selected_row, 0).text())
        cliente = session.query(Cliente).filter_by(id=id_cliente).first()

        if cliente:
            self.mod_cliente_view.lineEditNome.setText(cliente.nome)
            self.mod_cliente_view.lineEditCognome.setText(cliente.cognome)
            self.mod_cliente_view.lineEditTelefono.setText(cliente.telefono)
            self.mod_cliente_view.lineEditEmail.setText(cliente.email)
            self.mod_cliente_view.exec_()
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Cliente non trovato.")

    def edit_cliente(self):
        selected_row = self.view.tableClienti.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un cliente da modificare.")
            return

        id_cliente = int(self.view.tableClienti.item(selected_row, 0).text())
        cliente = session.query(Cliente).filter_by(id=id_cliente).first()

        if cliente:
            cliente.nome = self.mod_cliente_view.lineEditNome.text()
            cliente.cognome = self.mod_cliente_view.lineEditCognome.text()
            cliente.telefono = self.mod_cliente_view.lineEditTelefono.text()
            cliente.email = self.mod_cliente_view.lineEditEmail.text()

            session.commit()

            self.load_data()
            QtWidgets.QMessageBox.information(self.view, "Successo", "Cliente modificato con successo.")
            self.mod_cliente_view.accept()
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Cliente non trovato.")

    def cancel_mod_cliente(self):
        self.mod_cliente_view.reject()

    def delete_cliente(self):
        selected_row = self.view.tableClienti.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un cliente da eliminare.")
            return

        id_cliente = int(self.view.tableClienti.item(selected_row, 0).text())
        cliente = session.query(Cliente).filter_by(id=id_cliente).first()

        if cliente:
            session.delete(cliente)
            session.commit()
            self.load_data()
            QtWidgets.QMessageBox.information(self.view, "Successo", "Cliente eliminato con successo.")
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Cliente non trovato.")

    def show_scheda_cliente_dialog(self):
        selected_row = self.view.tableClienti.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un cliente per inserire la scheda.")
            return

        id_cliente = int(self.view.tableClienti.item(selected_row, 0).text())
        self.scheda_cliente_view.plainTextEditDescrizione.clear()
        self.scheda_cliente_view.listWidgetImages.clear()
        self.scheda_cliente_view.clear_graphics_view()
        self.current_scheda = None
        self.scheda_cliente_view.exec_()

    def add_scheda_cliente(self):
        selected_row = self.view.tableClienti.currentIndex().row()
        id_cliente = int(self.view.tableClienti.item(selected_row, 0).text())
        descrizione = self.scheda_cliente_view.plainTextEditDescrizione.toPlainText()
        immagini = [self.scheda_cliente_view.listWidgetImages.item(i).text() for i in range(self.scheda_cliente_view.listWidgetImages.count())]

        if self.current_scheda:
            scheda = self.current_scheda
            scheda.descrizione = descrizione
            session.query(ImmagineScheda).filter_by(id_scheda=scheda.id).delete()
        else:
            scheda = SchedaCliente(
                id_cliente=id_cliente,
                descrizione=descrizione
            )
            session.add(scheda)
            session.commit()

        for immagine in immagini:
            nuova_immagine = ImmagineScheda(
                id_scheda=scheda.id,
                percorso=immagine
            )
            session.add(nuova_immagine)

        session.commit()

        QtWidgets.QMessageBox.information(self.scheda_cliente_view, "Successo", "Scheda cliente inserita con successo.")
        self.scheda_cliente_view.accept()

    def cancel_scheda_cliente(self):
        self.scheda_cliente_view.reject()

    def show_scheda_cliente(self, id_cliente):
        scheda = session.query(SchedaCliente).filter_by(id_cliente=id_cliente).first()
        if scheda:
            self.current_scheda = scheda
            self.scheda_cliente_view.plainTextEditDescrizione.setPlainText(scheda.descrizione)
            self.scheda_cliente_view.listWidgetImages.clear()
            self.scheda_cliente_view.clear_graphics_view()
            for immagine in scheda.immagini:
                item = QListWidgetItem(immagine.percorso)
                self.scheda_cliente_view.listWidgetImages.addItem(item)
            self.scheda_cliente_view.exec_()
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Scheda cliente non trovata.")

    def show(self):
        self.view.show()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    controller = ClientiController()
    controller.show()
    sys.exit(app.exec_())