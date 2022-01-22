# This Python file uses the following encoding: utf-8
import json
from PySide6.QtWidgets import QMessageBox, QWidget, QListWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel, QIcon


class dataModel:
    def __init__(self):
        self.data = {}
        self.itemsModel = []
        try:
            f = open("data/data.json")
            try:
                self.data = json.load(f)
                f.close()
                self.initItemModel()
            except:
                QMessageBox.warning(QWidget(), "Error", "Invaild Json Data")
        except FileNotFoundError:
            self.updateToFile()
            self.initItemModel()

    def updateData(self,key,data):
        self.data[key] = data
        self.updateToFile()
        self.initItemModel()

    def updateDetails(self,key,subKey,data):
        self.data[key][subKey] = data
        self.updateToFile()

    def initItemModel(self):
        self.itemsModel.clear()
        for key in self.data.keys():
            self.itemsModel.append(QListWidgetItem(QIcon(":/icons/written_book.png"),key))
            print(self.itemsModel)

    def updateToFile(self):
        f = open("data/data.json", 'w')
        json.dump(self.data, f)
        f.close()
