# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\solar\Desktop\GestionAle1\Gest\views\ui\appuntamenti.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 730)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 781, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(22)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddAgenda = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddAgenda.sizePolicy().hasHeightForWidth())
        self.btnAddAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.btnAddAgenda.setFont(font)
        self.btnAddAgenda.setObjectName("btnAddAgenda")
        self.horizontalLayout_2.addWidget(self.btnAddAgenda)
        self.btnVisAgenda = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVisAgenda.sizePolicy().hasHeightForWidth())
        self.btnVisAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.btnVisAgenda.setFont(font)
        self.btnVisAgenda.setObjectName("btnVisAgenda")
        self.horizontalLayout_2.addWidget(self.btnVisAgenda)
        self.btnModifAgenda = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifAgenda.sizePolicy().hasHeightForWidth())
        self.btnModifAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.btnModifAgenda.setFont(font)
        self.btnModifAgenda.setObjectName("btnModifAgenda")
        self.horizontalLayout_2.addWidget(self.btnModifAgenda)
        self.btnElimAgenda = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnElimAgenda.sizePolicy().hasHeightForWidth())
        self.btnElimAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.btnElimAgenda.setFont(font)
        self.btnElimAgenda.setObjectName("btnElimAgenda")
        self.horizontalLayout_2.addWidget(self.btnElimAgenda)
        spacerItem = QtWidgets.QSpacerItem(408, 33, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboFiltraAgenda = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFiltraAgenda.sizePolicy().hasHeightForWidth())
        self.comboFiltraAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(11)
        font.setItalic(True)
        self.comboFiltraAgenda.setFont(font)
        self.comboFiltraAgenda.setObjectName("comboFiltraAgenda")
        self.comboFiltraAgenda.addItem("")
        self.comboFiltraAgenda.addItem("")
        self.comboFiltraAgenda.addItem("")
        self.comboFiltraAgenda.addItem("")
        self.comboFiltraAgenda.addItem("")
        self.horizontalLayout.addWidget(self.comboFiltraAgenda)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineCercaAgenda = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineCercaAgenda.sizePolicy().hasHeightForWidth())
        self.lineCercaAgenda.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setPointSize(12)
        font.setItalic(True)
        self.lineCercaAgenda.setFont(font)
        self.lineCercaAgenda.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineCercaAgenda.setClearButtonEnabled(True)
        self.lineCercaAgenda.setObjectName("lineCercaAgenda")
        self.horizontalLayout.addWidget(self.lineCercaAgenda)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 777, 530))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableAgendaEventi = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tableAgendaEventi.setGeometry(QtCore.QRect(390, 0, 391, 171))
        self.tableAgendaEventi.setAcceptDrops(False)
        self.tableAgendaEventi.setObjectName("tableAgendaEventi")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.scrollAreaWidgetContents_2)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 391, 171))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableAgenda = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tableAgenda.setGeometry(QtCore.QRect(0, 171, 781, 361))
        self.tableAgenda.setSortingEnabled(False)
        self.tableAgenda.setObjectName("tableAgenda")
        self.tableAgenda.horizontalHeader().setSortIndicatorShown(False)
        self.tableAgenda.horizontalHeader().setStretchLastSection(False)
        self.tableAgenda.verticalHeader().setCascadingSectionResizes(False)
        self.tableAgenda.verticalHeader().setSortIndicatorShown(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuNaviga = QtWidgets.QMenu(self.menubar)
        self.menuNaviga.setObjectName("menuNaviga")
        self.menuVisualizza = QtWidgets.QMenu(self.menubar)
        self.menuVisualizza.setObjectName("menuVisualizza")
        self.menuOpzioni = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setItalic(True)
        self.menuOpzioni.setFont(font)
        self.menuOpzioni.setObjectName("menuOpzioni")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Inria Serif")
        font.setItalic(True)
        self.menuInfo.setFont(font)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAgenda = QtWidgets.QAction(MainWindow)
        self.actionAgenda.setObjectName("actionAgenda")
        self.actionClienti = QtWidgets.QAction(MainWindow)
        self.actionClienti.setObjectName("actionClienti")
        self.actionInventario = QtWidgets.QAction(MainWindow)
        self.actionInventario.setObjectName("actionInventario")
        self.actionFatture = QtWidgets.QAction(MainWindow)
        self.actionFatture.setObjectName("actionFatture")
        self.actionDocumenti = QtWidgets.QAction(MainWindow)
        self.actionDocumenti.setObjectName("actionDocumenti")
        self.actionReport = QtWidgets.QAction(MainWindow)
        self.actionReport.setObjectName("actionReport")
        self.actionAggiungi = QtWidgets.QAction(MainWindow)
        self.actionAggiungi.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionAggiungi.setObjectName("actionAggiungi")
        self.actionVisualizza = QtWidgets.QAction(MainWindow)
        self.actionVisualizza.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionVisualizza.setObjectName("actionVisualizza")
        self.actionModifica = QtWidgets.QAction(MainWindow)
        self.actionModifica.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionModifica.setObjectName("actionModifica")
        self.actionElimina = QtWidgets.QAction(MainWindow)
        self.actionElimina.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionElimina.setObjectName("actionElimina")
        self.menuNaviga.addAction(self.actionAgenda)
        self.menuNaviga.addAction(self.actionClienti)
        self.menuNaviga.addAction(self.actionInventario)
        self.menuNaviga.addAction(self.actionFatture)
        self.menuNaviga.addAction(self.actionDocumenti)
        self.menuNaviga.addAction(self.actionReport)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuNaviga.menuAction())
        self.menubar.addAction(self.menuVisualizza.menuAction())
        self.menubar.addAction(self.menuOpzioni.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Agenda"))
        self.btnAddAgenda.setText(_translate("MainWindow", "Aggiungi"))
        self.btnVisAgenda.setText(_translate("MainWindow", "Visualizza"))
        self.btnModifAgenda.setText(_translate("MainWindow", "Modifica"))
        self.btnElimAgenda.setText(_translate("MainWindow", "Elimina"))
        self.comboFiltraAgenda.setCurrentText(_translate("MainWindow", "Scegli"))
        self.comboFiltraAgenda.setItemText(0, _translate("MainWindow", "Scegli"))
        self.comboFiltraAgenda.setItemText(1, _translate("MainWindow", "Select"))
        self.comboFiltraAgenda.setItemText(2, _translate("MainWindow", "prova"))
        self.comboFiltraAgenda.setItemText(3, _translate("MainWindow", "prova1"))
        self.comboFiltraAgenda.setItemText(4, _translate("MainWindow", "prova2"))
        self.lineCercaAgenda.setPlaceholderText(_translate("MainWindow", "Cerca..."))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuNaviga.setTitle(_translate("MainWindow", "Naviga"))
        self.menuVisualizza.setTitle(_translate("MainWindow", "Visualizza"))
        self.menuOpzioni.setTitle(_translate("MainWindow", "Opzioni"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionAgenda.setText(_translate("MainWindow", "Agenda"))
        self.actionClienti.setText(_translate("MainWindow", "Clienti"))
        self.actionInventario.setText(_translate("MainWindow", "Inventario"))
        self.actionFatture.setText(_translate("MainWindow", "Fatture"))
        self.actionDocumenti.setText(_translate("MainWindow", "Documenti"))
        self.actionReport.setText(_translate("MainWindow", "Report"))
        self.actionAggiungi.setText(_translate("MainWindow", "Aggiungi"))
        self.actionVisualizza.setText(_translate("MainWindow", "Visualizza"))
        self.actionModifica.setText(_translate("MainWindow", "Modifica"))
        self.actionElimina.setText(_translate("MainWindow", "Elimina"))
