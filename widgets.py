from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtWidgets import (QGridLayout, QPushButton, QStatusBar,
                             QTextBrowser, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 471))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.text_browser = QTextBrowser(self.widget)
        self.text_browser.setObjectName(u"text_browser")

        self.gridLayout.addWidget(self.text_browser, 0, 0, 1, 3)

        self.select_file_button = QPushButton(self.widget)
        self.select_file_button.setObjectName(u"select_file_button")

        self.gridLayout.addWidget(self.select_file_button, 1, 0, 1, 1)

        self.save_file_button = QPushButton(self.widget)
        self.save_file_button.setObjectName(u"save_file_button")

        self.gridLayout.addWidget(self.save_file_button, 1, 1, 1, 1)

        self.clear_button = QPushButton(self.widget)
        self.clear_button.setObjectName(u"clear_button")

        self.gridLayout.addWidget(self.clear_button, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.select_file_button.clicked.connect(MainWindow._select_file)
        self.save_file_button.clicked.connect(MainWindow._save_text)
        self.clear_button.clicked.connect(MainWindow._clear)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_file_button.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.save_file_button.setText(QCoreApplication.translate("MainWindow", u"Save text", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))