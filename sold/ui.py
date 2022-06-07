# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiyyjCbh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.send_pushButton = QPushButton(self.widget)
        self.send_pushButton.setObjectName(u"send_pushButton")
        self.send_pushButton.setGeometry(QRect(300, 250, 120, 30))
        self.send_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 15pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.brand_lineEdit = QLineEdit(self.widget)
        self.brand_lineEdit.setObjectName(u"brand_lineEdit")
        self.brand_lineEdit.setGeometry(QRect(100, 150, 113, 30))
        self.brand_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(300, 150, 113, 30))
        self.name_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.contact_lineEdit = QLineEdit(self.widget)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        self.contact_lineEdit.setGeometry(QRect(500, 150, 113, 30))
        self.contact_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 120, 100, 30))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 120, 100, 30))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 120, 120, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.send_pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Brand :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contact :", None))
    # retranslateUi

