# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uivPsfJq.ui'
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
        MainWindow.resize(800, 484)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 171, 30))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.search_tableWidget = QTableWidget(self.widget)
        self.search_tableWidget.setObjectName(u"search_tableWidget")
        self.search_tableWidget.setGeometry(QRect(10, 50, 750, 278))
        self.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 370, 120, 30))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.product_label = QLabel(self.widget)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setGeometry(QRect(10, 400, 150, 30))
        self.product_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.accept_pushButton = QPushButton(self.widget)
        self.accept_pushButton.setObjectName(u"accept_pushButton")
        self.accept_pushButton.setGeometry(QRect(500, 400, 120, 30))
        self.accept_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.reject_pushButton = QPushButton(self.widget)
        self.reject_pushButton.setObjectName(u"reject_pushButton")
        self.reject_pushButton.setGeometry(QRect(630, 400, 120, 30))
        self.reject_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.price_lineEdit = QLineEdit(self.widget)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setGeometry(QRect(180, 400, 120, 30))
        self.price_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.state_lineEdit = QLineEdit(self.widget)
        self.state_lineEdit.setObjectName(u"state_lineEdit")
        self.state_lineEdit.setGeometry(QRect(310, 400, 120, 30))

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Search Result", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Product_ID :", None))
        self.product_label.setText("")
        self.accept_pushButton.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.reject_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
    # retranslateUi

