# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import QObject, SignalInstance, Signal, Slot, QDate, QTimer, QModelIndex
from PySide6.QtGui import QFont, QIcon
import icons_rc
import newDialog, dataModel, record
import threading, time
import AI

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.datamodel = dataModel.dataModel()
        self.updateListWidget()
        self.ui.listWidget.itemClicked.connect(self.listWidgets_itemClicked)
        self.ui.frame_4.hide()
        self.ui.frame_3.hide()
        self.ui.frame_5.hide()
        self.ui.statusBar.showMessage("Initing Recording Module...")
        self.setFont(QFont(":/fonts/Inter-Regular.otf"))
        self.singal = Communicate()
        self.singal.dataChanged.connect(self.getDetails)
        self.recorder = record.record()
        self.recorder.signal.finished.connect(self.finishedInit)
        self.inited = False
        t2 = threading.Thread(target=self.recorder.initPyaduio,daemon=True)
        t2.start()
        self.ai = AI.AI()
#        self.ui.frame_4.show()

    @Slot()
    def finishedInit(self):
        self.ui.statusBar.showMessage("Ready")
        self.inited = True
        self.ui.recordBtn.setEnabled(True)
        self.ui.recordBtn.setIcon(QIcon(":/icons/mic_black_48dp.svg"))



    @Slot()
    def on_actionNewDia_triggered(self):
        newdia = newDialog.newDialog()
        newdia.someone.data.connect(self.processData)
        newdia.exec()

    @Slot()
    def processData(self, data):
        self.ui.frame_3.hide()
        self.ui.frame_5.hide()
        self.ui.frame_4.hide()
        self.ui.listWidget.clear()
        self.datamodel.updateData(data["Time"],data)
        self.updateListWidget()

    @Slot()
    def on_recordBtn_clicked(self):
        if self.inited:
            self.ui.frame_5.hide()
            self.ui.frame_3.show()
            self.starttime = time.time()
            t1 = threading.Thread(target=self.recorder.record_audio,args=tuple(["data/record/"+self.currentItem+".wav"]),daemon=True)
            t1.start()
            self.timer = QTimer(self)
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.updateTimer)
            self.timer.start()

    @Slot()
    def updateTimer(self):
        print(time.time() - self.starttime)
        deltaTime = time.time() - self.starttime
        self.ui.timeLabel.setText(self.secToMins(deltaTime))


    @Slot()
    def on_stopBtn_clicked(self):
        self.recorder.stopRecording()
        self.timer.stop()
        self.datamodel.updateDetails(self.currentItem,"Path","data/record/"+self.currentItem+".wav")
        print(self.datamodel.data)
        self.ui.frame_3.hide()
        self.ui.frame_4.show()
        self.clearDetails()
        t1 = threading.Thread(target=self.startASR,args=tuple(["data/record/"+self.currentItem+".wav"]),daemon=True)
        t1.start()

    @Slot()
    def on_playBtn_clicked(self):
        t1 = threading.Thread(target=self.recorder.playRecording,args=(tuple(["data/record/"+self.currentItem+".wav"])),daemon=True)
        t1.start()

    @Slot()
    def listWidgets_itemClicked(self,item):
        key = item.text()
        self.currentItem = key
        print(key)
        if ("Path" in self.datamodel.data[key]):
            self.singal.dataChanged.emit()
            self.ui.frame_3.hide()
            self.ui.frame_5.hide()
            self.ui.frame_4.show()

        else:
            self.ui.frame_3.hide()
            self.ui.frame_5.show()
            self.ui.frame_4.hide()

    def secToMins(self,sec):
        secInt = round(sec)
        return str(secInt // 60).zfill(2) + ":" + str(secInt % 60).zfill(2)

    def updateListWidget(self):
        for item in self.datamodel.itemsModel:
            print(item.text())
            self.ui.listWidget.addItem(item)

    def startASR(self,filename):
        self.ui.statusBar.showMessage("Analyzing your Dairy...")
        self.result = self.ai.getTranscript(filename)
        self.datamodel.updateDetails(self.currentItem,"Transcript",self.result['text'])
        try:
            keywordsList = []
            for word in self.result["auto_highlights_result"]["results"]:
                keywordsList.append(word["text"])
            self.datamodel.updateDetails(self.currentItem,"Keywords",keywordsList)
        except:
            self.datamodel.updateDetails(self.currentItem,"Keywords",["No Key Word"])
        self.singal.dataChanged.emit()
        self.ui.statusBar.showMessage("Ready")
        print(type(self.result))

    @Slot()
    def getDetails(self):
        self.ui.plainTextEdit.setPlainText(self.datamodel.data[self.currentItem]["Transcript"])
        self.ui.label.setText(", ".join(self.datamodel.data[self.currentItem]["Keywords"]))
        if(self.datamodel.data[self.currentItem]["Feeling"] == "Good"):
            self.ui.pushButton.setIcon(QIcon(":/icons/Cowboy hat face.svg"))
        elif(self.datamodel.data[self.currentItem]["Feeling"] == "Sad"):
            self.ui.pushButton.setIcon(QIcon(":/icons/Dissapointed face.svg"))
        else:
            self.ui.pushButton.setIcon(QIcon(":/icons/Neutral face.svg"))

    def clearDetails(self):
        self.ui.plainTextEdit.setPlainText("")
        self.ui.label.setText("")
        if(self.datamodel.data[self.currentItem]["Feeling"] == "Good"):
            self.ui.pushButton.setIcon(QIcon(":/icons/Cowboy hat face.svg"))
        elif(self.datamodel.data[self.currentItem]["Feeling"] == "Sad"):
            self.ui.pushButton.setIcon(QIcon(":/icons/Dissapointed face.svg"))
        else:
            self.ui.pushButton.setIcon(QIcon(":/icons/Neutral face.svg"))

class Communicate(QObject):
    dataChanged = Signal()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



