# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 497)
        self.action_local_save = QAction(MainWindow)
        self.action_local_save.setObjectName(u"action_local_save")
        self.action_remote_save = QAction(MainWindow)
        self.action_remote_save.setObjectName(u"action_remote_save")
        self.action_remote_load = QAction(MainWindow)
        self.action_remote_load.setObjectName(u"action_remote_load")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 591, 371))
        self.imageLabel = QLabel(self.groupBox)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(10, 20, 561, 201))
        self.imageLabel.setStyleSheet(u"border: 1px solid rgb(0, 0, 0);")
        self.imageLabel.setFrameShape(QFrame.NoFrame)
        self.imageLabel.setLineWidth(6)
        self.imageLabel.setMidLineWidth(4)
        self.imageLabel.setWordWrap(False)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 320, 431, 31))
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(490, 320, 75, 31))
        self.originEdit = QLineEdit(self.groupBox)
        self.originEdit.setObjectName(u"originEdit")
        self.originEdit.setGeometry(QRect(50, 280, 431, 31))
        self.originEdit.setReadOnly(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 290, 31, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 330, 31, 16))
        self.restoreButton = QPushButton(self.groupBox)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setGeometry(QRect(490, 280, 75, 31))
        self.preEdit = QLineEdit(self.groupBox)
        self.preEdit.setObjectName(u"preEdit")
        self.preEdit.setGeometry(QRect(50, 240, 431, 31))
        self.preEdit.setReadOnly(True)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 250, 31, 16))
        self.preLabel = QLabel(self.groupBox)
        self.preLabel.setObjectName(u"preLabel")
        self.preLabel.setGeometry(QRect(515, 230, 31, 16))
        self.probLabel = QLabel(self.groupBox)
        self.probLabel.setObjectName(u"probLabel")
        self.probLabel.setGeometry(QRect(493, 250, 71, 20))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(610, 10, 120, 371))
        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 111, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.uncertainBox = QCheckBox(self.verticalLayoutWidget)
        self.uncertainBox.setObjectName(u"uncertainBox")

        self.verticalLayout.addWidget(self.uncertainBox)

        self.invalidBox = QCheckBox(self.verticalLayoutWidget)
        self.invalidBox.setObjectName(u"invalidBox")

        self.verticalLayout.addWidget(self.invalidBox)

        self.punctuationBox = QCheckBox(self.verticalLayoutWidget)
        self.punctuationBox.setObjectName(u"punctuationBox")

        self.verticalLayout.addWidget(self.punctuationBox)

        self.symbolBox = QCheckBox(self.verticalLayoutWidget)
        self.symbolBox.setObjectName(u"symbolBox")

        self.verticalLayout.addWidget(self.symbolBox)

        self.spaceBox = QCheckBox(self.verticalLayoutWidget)
        self.spaceBox.setObjectName(u"spaceBox")

        self.verticalLayout.addWidget(self.spaceBox)

        self.alienBox = QCheckBox(self.verticalLayoutWidget)
        self.alienBox.setObjectName(u"alienBox")

        self.verticalLayout.addWidget(self.alienBox)

        self.traditionalBox = QCheckBox(self.verticalLayoutWidget)
        self.traditionalBox.setObjectName(u"traditionalBox")

        self.verticalLayout.addWidget(self.traditionalBox)

        self.clarityBox = QComboBox(self.groupBox_2)
        self.clarityBox.addItem("")
        self.clarityBox.addItem("")
        self.clarityBox.addItem("")
        self.clarityBox.addItem("")
        self.clarityBox.addItem("")
        self.clarityBox.setObjectName(u"clarityBox")
        self.clarityBox.setGeometry(QRect(60, 328, 51, 22))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 330, 54, 16))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 390, 721, 61))
        self.lastButton = QPushButton(self.groupBox_3)
        self.lastButton.setObjectName(u"lastButton")
        self.lastButton.setGeometry(QRect(10, 20, 75, 31))
        self.nextButton = QPushButton(self.groupBox_3)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(100, 20, 75, 31))
        self.lastUButton = QPushButton(self.groupBox_3)
        self.lastUButton.setObjectName(u"lastUButton")
        self.lastUButton.setGeometry(QRect(190, 20, 91, 31))
        self.nextUButton = QPushButton(self.groupBox_3)
        self.nextUButton.setObjectName(u"nextUButton")
        self.nextUButton.setGeometry(QRect(290, 20, 91, 31))
        self.jumptextLabel = QLabel(self.groupBox_3)
        self.jumptextLabel.setObjectName(u"jumptextLabel")
        self.jumptextLabel.setGeometry(QRect(400, 30, 54, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(460, 30, 113, 20))
        self.jumpButton = QPushButton(self.groupBox_3)
        self.jumpButton.setObjectName(u"jumpButton")
        self.jumpButton.setGeometry(QRect(580, 20, 51, 31))
        self.openButton = QPushButton(self.groupBox_3)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setGeometry(QRect(640, 20, 75, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 741, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_local_save)
        self.menu.addAction(self.action_remote_save)
        self.menu.addAction(self.action_remote_load)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCR\u8bc6\u522b\u6807\u6ce8 by HIT-DimWeaker", None))
        self.action_local_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230\u672c\u5730", None))
        self.action_remote_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230\u670d\u52a1\u5668", None))
        self.action_remote_load.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u670d\u52a1\u5668\u8bfb\u53d6", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u6ce8\u533a", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u56fe\u7247</p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65e7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\uff1a", None))
        self.restoreButton.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u539f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\uff1a", None))
        self.preLabel.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1", None))
        self.probLabel.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u8bb0\u533a", None))
        self.uncertainBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u786e\u5b9a", None))
        self.invalidBox.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u6548\u4fe1\u606f", None))
        self.punctuationBox.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6807\u70b9", None))
        self.symbolBox.setText(QCoreApplication.translate("MainWindow", u"\u6709\u7279\u6b8a\u7b26\u53f7", None))
        self.spaceBox.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u80fd\u6709\u7a7a\u683c", None))
        self.alienBox.setText(QCoreApplication.translate("MainWindow", u"\u5f02\u5f62\u6587\u5b57", None))
        self.traditionalBox.setText(QCoreApplication.translate("MainWindow", u"\u7e41\u4f53\u5b57", None))
        self.clarityBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.clarityBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2 ", None))
        self.clarityBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.clarityBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.clarityBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u6670\u5ea6\uff1a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u533a", None))
        self.lastButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.lastUButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20\u672a\u6807\u6ce8", None))
        self.nextUButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20\u672a\u6807\u6ce8", None))
        self.jumptextLabel.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c\u7f16\u53f7\uff1a", None))
        self.lineEdit_2.setInputMask("")
        self.jumpButton.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u67e5\u770b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

