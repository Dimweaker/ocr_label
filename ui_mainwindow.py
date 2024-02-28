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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 457)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 591, 331))
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
        self.lineEdit.setGeometry(QRect(50, 280, 431, 31))
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(490, 280, 75, 31))
        self.originEdit = QLineEdit(self.groupBox)
        self.originEdit.setObjectName(u"originEdit")
        self.originEdit.setGeometry(QRect(50, 240, 431, 31))
        self.originEdit.setReadOnly(True)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 250, 31, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 290, 31, 16))
        self.restoreButton = QPushButton(self.groupBox)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setGeometry(QRect(490, 240, 75, 31))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(610, 10, 120, 331))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 350, 721, 61))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 741, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u6ce8\u533a", None))
        self.imageLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u56fe\u7247</p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65e7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65b0\uff1a", None))
        self.restoreButton.setText(QCoreApplication.translate("MainWindow", u"\u8fd8\u539f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879\u533a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u533a", None))
        self.lastButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.lastUButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20\u672a\u6807\u6ce8", None))
        self.nextUButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20\u672a\u6807\u6ce8", None))
        self.jumptextLabel.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c\u7f16\u53f7\uff1a", None))
        self.lineEdit_2.setInputMask("")
        self.jumpButton.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8f6c", None))
    # retranslateUi

