import sys
import subprocess
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QIcon
from ui_mainwindow import *
from manager import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.manager = Manager()

        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.probLabel.setAlignment(QtCore.Qt.AlignCenter)

        icon = QIcon('logo.bmp')
        self.setWindowIcon(icon)

        self.lastButton.clicked.connect(self.last)
        self.nextButton.clicked.connect(self.next)
        self.lastUButton.clicked.connect(self.last_unchanged)
        self.nextUButton.clicked.connect(self.next_unchanged)
        self.saveButton.clicked.connect(self.local_save)
        self.restoreButton.clicked.connect(self.restore)
        self.jumpButton.clicked.connect(self.jump)
        self.openButton.clicked.connect(self.open)
        self.action_local_save.triggered.connect(self.local_save)
        self.action_remote_load.triggered.connect(self.remote_load)
        self.action_remote_save.triggered.connect(self.remote_save)

        self.scaled_ratio = 1.0

        self.show_data()

    def show_data(self, show_image=True):
        image_path = self.manager.image_path
        text_label = self.manager.text_label
        text_label_origin = self.manager.text_label_origin
        prediction_text_label = self.manager.prediction_text_label
        prediction_score = self.manager.prediction_score
        uncertain = self.manager.uncertain
        invalid = self.manager.invalid
        punctuation = self.manager.punctuation
        symbol = self.manager.symbol
        space = self.manager.space
        clarity = self.manager.clarity
        time = self.manager.time
        user = self.manager.user

        self.uncertainBox.setChecked(uncertain)
        self.invalidBox.setChecked(invalid)
        self.punctuationBox.setChecked(punctuation)
        self.symbolBox.setChecked(symbol)
        self.spaceBox.setChecked(space)
        self.clarityBox.setCurrentIndex(clarity - 1)

        self.preEdit.setText(prediction_text_label)
        self.probLabel.setText(f"{prediction_score:.4f}")
        self.originEdit.setText(text_label_origin)
        self.lineEdit.setText(text_label)
        self.statusBar().showMessage(
            f"{self.manager.index + 1}/{len(self.manager.data)}\t{image_path}\tchanged: {self.manager.is_changed(self.manager.index)}\t{user}\t{time}"
        )
        if show_image:
            self.show_image()

    def show_image(self):
        image_path = self.manager.image_path
        image = QPixmap(image_path)

        label_width = self.imageLabel.width()
        label_height = self.imageLabel.height()

        image_ratio = image.width() / image.height()
        label_ratio = label_width / label_height

        if image_ratio >= label_ratio:
            image = image.scaled(label_width * self.scaled_ratio,
                                 label_width / image_ratio * self.scaled_ratio)
        else:
            image = image.scaled(label_height * image_ratio * self.scaled_ratio,
                                 label_height * self.scaled_ratio)

        self.imageLabel.setPixmap(image)

    def local_save(self):
        text = self.lineEdit.text()
        uncertain = self.uncertainBox.isChecked()
        invalid = self.invalidBox.isChecked()
        punctuation = self.punctuationBox.isChecked()
        symbol = self.symbolBox.isChecked()
        space = self.spaceBox.isChecked()
        clarity = self.clarityBox.currentIndex() + 1

        self.manager.change(text, uncertain, invalid, punctuation, symbol, space, clarity)
        self.show_data(show_image=False)

    def restore(self):
        self.manager.restore()
        self.show_data(show_image=False)

    def remote_load(self):
        self.manager.remote_load()
        self.show_data()

    def remote_save(self):
        self.manager.remote_save()
        self.show_data()

    def next(self):
        if self.manager.index == len(self.manager.data) - 1:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("This is the last image")
            msg.exec()
            return
        self.manager.index += 1
        self.show_data()

    def last(self):
        if self.manager.index == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("This is the first image")
            msg.exec()
            return
        self.manager.index -= 1
        self.show_data()

    def next_unchanged(self):
        self.manager.next_unchanged()
        self.show_data()

    def last_unchanged(self):
        self.manager.last_unchanged()
        self.show_data()

    def jump(self):
        image = eval(self.lineEdit_2.text())
        if self.manager.jump(image) is not None:
            self.show_data()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"Image {image} not found")
            msg.exec()

    def open(self):
        try:
            subprocess.Popen(['start', self.manager.image_path], shell=True)
        except Exception as e:
            print(e)

    def keyPressEvent(self, event):
        modifiers = event.modifiers()
        if modifiers == QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_S:
                self.local_save()
            if event.key() == QtCore.Qt.Key_L:
                self.restore()

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scaled_ratio *= 1.1
            if self.scaled_ratio > 1:
                self.scaled_ratio = 1.0
        else:
            self.scaled_ratio /= 1.1
            if self.scaled_ratio < 0.1:
                self.scaled_ratio = 0.1
        self.show_image()

    def closeEvent(self, event):
        self.manager.save()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
