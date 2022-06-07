# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiqYPIdS.ui'
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
        self.label_8.setGeometry(QRect(10, 60, 171, 30))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.search_tableWidget = QTableWidget(self.widget)
        self.search_tableWidget.setObjectName(u"search_tableWidget")
        self.search_tableWidget.setGeometry(QRect(10, 100, 750, 278))
        self.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 390, 120, 30))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.product_label = QLabel(self.widget)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setGeometry(QRect(10, 420, 120, 30))
        self.product_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.accept_pushButton = QPushButton(self.widget)
        self.accept_pushButton.setObjectName(u"accept_pushButton")
        self.accept_pushButton.setGeometry(QRect(500, 420, 120, 30))
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
        self.reject_pushButton.setGeometry(QRect(630, 420, 120, 30))
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
        self.price_lineEdit.setGeometry(QRect(150, 420, 90, 30))
        self.price_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.state_lineEdit = QLineEdit(self.widget)
        self.state_lineEdit.setObjectName(u"state_lineEdit")
        self.state_lineEdit.setGeometry(QRect(250, 420, 90, 30))
        self.state_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 390, 120, 30))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 390, 58, 30))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.class_comboBox = QComboBox(self.widget)
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setGeometry(QRect(350, 420, 100, 30))
        self.class_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.employee_comboBox = QComboBox(self.widget)
        self.employee_comboBox.setObjectName(u"employee_comboBox")
        self.employee_comboBox.setGeometry(QRect(370, 20, 120, 30))
        self.employee_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 20, 120, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Price :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"State :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Employee :", None))
    # retranslateUi

