# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(776, 474)
        icon = QIcon()
        icon.addFile(u":/icons/writable_book.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionNewDia = QAction(MainWindow)
        self.actionNewDia.setObjectName(u"actionNewDia")
        self.actionNewDia.setCheckable(False)
        self.actionNewDia.setChecked(False)
        self.actionNewDia.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/post_add_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewDia.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.Box)
        self.listWidget.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(600, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.pushButton.setIconSize(QSize(96, 96))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.plainTextEdit = QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEdit)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.time1 = QLabel(self.frame_7)
        self.time1.setObjectName(u"time1")

        self.horizontalLayout_3.addWidget(self.time1)

        self.horizontalSlider = QSlider(self.frame_7)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.time2 = QLabel(self.frame_7)
        self.time2.setObjectName(u"time2")

        self.horizontalLayout_3.addWidget(self.time2)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.playBtn = QPushButton(self.frame_4)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/play_circle_filled_black_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon2)
        self.playBtn.setIconSize(QSize(48, 48))

        self.verticalLayout_3.addWidget(self.playBtn)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(22)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.recordBtn = QPushButton(self.frame_5)
        self.recordBtn.setObjectName(u"recordBtn")
        self.recordBtn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.recordBtn.sizePolicy().hasHeightForWidth())
        self.recordBtn.setSizePolicy(sizePolicy1)
        self.recordBtn.setAutoFillBackground(False)
        self.recordBtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/mic_black_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordBtn.setIcon(icon3)
        self.recordBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_2.addWidget(self.recordBtn)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.timeLabel = QLabel(self.frame_3)
        self.timeLabel.setObjectName(u"timeLabel")
        sizePolicy4.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy4)
        self.timeLabel.setFont(font2)
        self.timeLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.timeLabel)

        self.stopBtn = QPushButton(self.frame_3)
        self.stopBtn.setObjectName(u"stopBtn")
        sizePolicy1.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy1)
        self.stopBtn.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/stop_black_48dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBtn.setIcon(icon4)
        self.stopBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_4.addWidget(self.stopBtn)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 776, 25))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.toolBar.addAction(self.actionNewDia)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI Voice Diary", None))
        self.actionNewDia.setText(QCoreApplication.translate("MainWindow", u"New Dairy", None))
#if QT_CONFIG(tooltip)
        self.actionNewDia.setToolTip(QCoreApplication.translate("MainWindow", u"New Dairy", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Daily Key Words: ", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.time1.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.time2.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.playBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Let's Start!", None))
        self.recordBtn.setText("")
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.stopBtn.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

