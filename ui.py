# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiJRmsof.ui'
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
        MainWindow.resize(1024, 900)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.brand_comboBox = QComboBox(self.widget_2)
        self.brand_comboBox.setObjectName(u"brand_comboBox")
        self.brand_comboBox.setGeometry(QRect(172, 20, 154, 30))
        self.brand_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.price_comboBox = QComboBox(self.widget_2)
        self.price_comboBox.setObjectName(u"price_comboBox")
        self.price_comboBox.setGeometry(QRect(333, 20, 153, 30))
        self.price_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.search_pushButton = QPushButton(self.widget_2)
        self.search_pushButton.setObjectName(u"search_pushButton")
        self.search_pushButton.setGeometry(QRect(815, 20, 154, 30))
        font = QFont()
        font.setFamily(u"Rockwell")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.secondhand_checkBox = QCheckBox(self.widget_2)
        self.secondhand_checkBox.setObjectName(u"secondhand_checkBox")
        self.secondhand_checkBox.setGeometry(QRect(493, 20, 154, 30))
        self.secondhand_checkBox.setFont(font)
        self.secondhand_checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.recommend_checkBox = QCheckBox(self.widget_2)
        self.recommend_checkBox.setObjectName(u"recommend_checkBox")
        self.recommend_checkBox.setGeometry(QRect(654, 20, 154, 30))
        self.recommend_checkBox.setFont(font)
        self.recommend_checkBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.class_comboBox = QComboBox(self.widget_2)
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setGeometry(QRect(11, 20, 154, 30))
        self.class_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_tableWidget = QTableWidget(self.widget_3)
        self.search_tableWidget.setObjectName(u"search_tableWidget")
        self.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_3.addWidget(self.search_tableWidget)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.add_pushButton = QPushButton(self.widget_4)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setGeometry(QRect(735, 20, 234, 30))
        self.add_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.product_label = QLabel(self.widget_4)
        self.product_label.setObjectName(u"product_label")
        self.product_label.setGeometry(QRect(252, 20, 235, 30))
        self.product_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.count_comboBox = QComboBox(self.widget_4)
        self.count_comboBox.setObjectName(u"count_comboBox")
        self.count_comboBox.setGeometry(QRect(494, 20, 234, 30))
        self.count_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.user_comboBox = QComboBox(self.widget_4)
        self.user_comboBox.setObjectName(u"user_comboBox")
        self.user_comboBox.setGeometry(QRect(11, 20, 234, 30))
        self.user_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cart_tableWidget = QTableWidget(self.widget_5)
        self.cart_tableWidget.setObjectName(u"cart_tableWidget")
        self.cart_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_2.addWidget(self.cart_tableWidget)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.order_pushButton = QPushButton(self.widget_6)
        self.order_pushButton.setObjectName(u"order_pushButton")
        self.order_pushButton.setGeometry(QRect(735, 20, 234, 30))
        self.order_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.delete_pushButton = QPushButton(self.widget_6)
        self.delete_pushButton.setObjectName(u"delete_pushButton")
        self.delete_pushButton.setGeometry(QRect(494, 20, 234, 30))
        self.delete_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
" font: 10pt \"Rockwell\"; \n"
"background-color: rgb(60, 60, 60); \n"
"font: bold; \n"
"border: 1px solid silver; \n"
"border-radius: 6px;\n"
"subcontrol-origin:  margin; \n"
"padding: 2 2px 2 2px;")
        self.delete_label = QLabel(self.widget_6)
        self.delete_label.setObjectName(u"delete_label")
        self.delete_label.setGeometry(QRect(252, 20, 235, 30))
        self.delete_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")

        self.verticalLayout.addWidget(self.widget_6)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 1)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.secondhand_checkBox.setText(QCoreApplication.translate("MainWindow", u"Second Hand", None))
        self.recommend_checkBox.setText(QCoreApplication.translate("MainWindow", u"Recommend", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.product_label.setText("")
        self.order_pushButton.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.delete_label.setText("")
    # retranslateUi

