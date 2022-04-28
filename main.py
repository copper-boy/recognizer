import sys

import pytesseract
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from widgets import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def _select_file(self):
        file, check = QFileDialog.getOpenFileName(self, 'Open File', './', 'Image (*.png *.jpg *jpeg)')

        if check:
            self.__add_text(MainWindow.__recognize_text(file))
        else:
            QMessageBox.critical(self, 'Critical', 'Select any file')

    def _clear(self):
        self.text_browser.clear()

    def _save_text(self):
        file, check = QFileDialog.getSaveFileName(self, 'Save File', './', 'All files (*);; Text files (*.txt)')
        text = self.text_browser.toPlainText()

        if check and text:
            with open(file, 'w+') as f:
                f.write(self.text_browser.toPlainText())
        else:
            QMessageBox.critical(self, 'Critical', 'Enter file name')

    def __add_text(self, text: str) -> None:
        self.text_browser.append(text)

    @staticmethod
    def __recognize_text(file: str) -> str:
        return pytesseract.image_to_string(Image.open(file))


def main():
    application = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(application.exec())


if __name__ == "__main__":
    main()
