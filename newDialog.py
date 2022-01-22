# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from ui_dialog import Ui_Dialog
from PySide6.QtCore import QObject, SignalInstance, Signal, Slot
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QDateTimeEdit
from PySide6.QtGui import QFont


class newDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.data = {}
        self.someone = Communicate()
        self.setFont(QFont(":/fonts/Inter-Regular.otf"))

    @Slot()
    def on_pushButton_clicked(self):
        self.data["Feeling"] = "Sad"
        self.data["Time"] = self.ui.dateEdit.date().toString("yyyy_MM_dd")
        self.someone.data.emit(self.data)
        self.accept()

    @Slot()
    def on_pushButton_2_clicked(self):
        self.data["Feeling"] = "Normal"
        self.data["Time"] = self.ui.dateEdit.date().toString("yyyy_MM_dd")
        self.someone.data.emit(self.data)
        self.accept()

    @Slot()
    def on_pushButton_3_clicked(self):
        self.data["Feeling"] = "Good"
        self.data["Time"] = self.ui.dateEdit.date().toString("yyyy_MM_dd")
        self.someone.data.emit(self.data)
        self.accept()


class Communicate(QObject):
    data = Signal(dict)
