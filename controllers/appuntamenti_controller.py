from views.appuntamenti_view import AppuntamentiView
from models.appuntamenti_model import Appuntamento
from database.setup import session
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDate, QTime

class AppuntamentiController:
    def __init__(self):
        self.view = AppuntamentiView()
        self.modelAgenda = QtGui.QStandardItemModel()
        self.modelEventi = QtGui.QStandardItemModel()
        self.view.tableAgenda.setModel(self.modelAgenda)
        self.view.tableAgendaEventi.setModel(self.modelEventi)
        self.load_data()
        self.connect_signals()

    def load_data(self):
        self.modelAgenda.clear()
        self.modelAgenda.setHorizontalHeaderLabels(["Ora", "Evento"])
        self.modelEventi.clear()
        self.modelEventi.setHorizontalHeaderLabels(["ID", "ID Cliente", "Data", "Ora", "Durata", "Trattamento", "Note"])
        
        # Popola la tabella degli orari
        for hour in range(24):
            items = [
                QtGui.QStandardItem(f"{hour:02d}:00"),
                QtGui.QStandardItem("")
            ]
            self.modelAgenda.appendRow(items)

        # Carica gli appuntamenti dal database
        self.load_appointments()

    def load_appointments(self):
        selected_date = self.view.calendarWidget.selectedDate().toPyDate()
        appuntamenti = session.query(Appuntamento).filter_by(data=selected_date).all()
        for appuntamento in appuntamenti:
            row = appuntamento.ora.hour()
            self.modelAgenda.setItem(row, 1, QtGui.QStandardItem(appuntamento.trattamento))

    def connect_signals(self):
        self.view.btnAddAgenda.clicked.connect(self.add_appuntamento)
        self.view.btnVisAgenda.clicked.connect(self.view_appuntamento)
        self.view.btnModifAgenda.clicked.connect(self.edit_appuntamento)
        self.view.btnElimAgenda.clicked.connect(self.delete_appuntamento)
        self.view.calendarWidget.selectionChanged.connect(self.load_appointments)
        self.view.tableAgenda.clicked.connect(self.show_event_details)

    def add_appuntamento(self):
        id_cliente = int(self.view.lineEditIdCliente.text())
        data = self.view.calendarWidget.selectedDate().toPyDate()
        ora = self.view.timeEditOra.time().toPyTime()
        durata = int(self.view.spinBoxDurata.value())
        trattamento = self.view.lineEditTrattamento.text()
        note = self.view.textEditNote.toPlainText()

        nuovo_appuntamento = Appuntamento(
            id_cliente=id_cliente,
            data=data,
            ora=ora,
            durata=durata,
            trattamento=trattamento,
            note=note
        )
        session.add(nuovo_appuntamento)
        session.commit()

        self.load_appointments()
        QtWidgets.QMessageBox.information(self.view, "Successo", "Appuntamento aggiunto con successo.")

    def view_appuntamento(self):
        selected_row = self.view.tableAgenda.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un orario per visualizzare l'evento.")
            return

        selected_date = self.view.calendarWidget.selectedDate().toPyDate()
        ora = QTime(selected_row, 0)
        appuntamento = session.query(Appuntamento).filter_by(data=selected_date, ora=ora).first()

        if appuntamento:
            self.modelEventi.clear()
            self.modelEventi.setHorizontalHeaderLabels(["ID", "ID Cliente", "Data", "Ora", "Durata", "Trattamento", "Note"])
            items = [
                QtGui.QStandardItem(str(appuntamento.id)),
                QtGui.QStandardItem(str(appuntamento.id_cliente)),
                QtGui.QStandardItem(str(appuntamento.data)),
                QtGui.QStandardItem(str(appuntamento.ora)),
                QtGui.QStandardItem(str(appuntamento.durata)),
                QtGui.QStandardItem(appuntamento.trattamento),
                QtGui.QStandardItem(appuntamento.note)
            ]
            self.modelEventi.appendRow(items)
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Nessun evento trovato per l'orario selezionato.")

    def edit_appuntamento(self):
        selected_row = self.view.tableAgendaEventi.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un evento da modificare.")
            return

        id_appuntamento = int(self.modelEventi.item(selected_row, 0).text())
        appuntamento = session.query(Appuntamento).filter_by(id=id_appuntamento).first()

        if appuntamento:
            id_cliente = int(self.view.lineEditIdCliente.text())
            data = self.view.calendarWidget.selectedDate().toPyDate()
            ora = self.view.timeEditOra.time().toPyTime()
            durata = int(self.view.spinBoxDurata.value())
            trattamento = self.view.lineEditTrattamento.text()
            note = self.view.textEditNote.toPlainText()

            appuntamento.id_cliente = id_cliente
            appuntamento.data = data
            appuntamento.ora = ora
            appuntamento.durata = durata
            appuntamento.trattamento = trattamento
            appuntamento.note = note

            session.commit()

            self.load_appointments()
            QtWidgets.QMessageBox.information(self.view, "Successo", "Appuntamento modificato con successo.")
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Appuntamento non trovato.")

    def delete_appuntamento(self):
        selected_row = self.view.tableAgendaEventi.currentIndex().row()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Seleziona un evento da eliminare.")
            return

        id_appuntamento = int(self.modelEventi.item(selected_row, 0).text())
        appuntamento = session.query(Appuntamento).filter_by(id=id_appuntamento).first()

        if appuntamento:
            session.delete(appuntamento)
            session.commit()
            self.load_appointments()
            QtWidgets.QMessageBox.information(self.view, "Successo", "Appuntamento eliminato con successo.")
        else:
            QtWidgets.QMessageBox.warning(self.view, "Errore", "Appuntamento non trovato.")

    def show_event_details(self):
        selected_row = self.view.tableAgenda.currentIndex().row()
        if selected_row == -1:
            return

        selected_date = self.view.calendarWidget.selectedDate().toPyDate()
        ora = QTime(selected_row, 0)
        appuntamento = session.query(Appuntamento).filter_by(data=selected_date, ora=ora).first()

        if appuntamento:
            self.modelEventi.clear()
            self.modelEventi.setHorizontalHeaderLabels(["ID", "ID Cliente", "Data", "Ora", "Durata", "Trattamento", "Note"])
            items = [
                QtGui.QStandardItem(str(appuntamento.id)),
                QtGui.QStandardItem(str(appuntamento.id_cliente)),
                QtGui.QStandardItem(str(appuntamento.data)),
                QtGui.QStandardItem(str(appuntamento.ora)),
                QtGui.QStandardItem(str(appuntamento.durata)),
                QtGui.QStandardItem(appuntamento.trattamento),
                QtGui.QStandardItem(appuntamento.note)
            ]
            self.modelEventi.appendRow(items)

    def show(self):
        self.view.show()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    controller = AppuntamentiController()
    controller.show()
    sys.exit(app.exec_())