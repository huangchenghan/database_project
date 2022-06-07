# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uisXlEFC.ui'
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
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(11, 50, 980, 64))
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
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(15, 0, 90, 15))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(175, 0, 90, 15))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(335, 0, 90, 15))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(11, 150, 958, 300))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_tableWidget = QTableWidget(self.widget_3)
        self.search_tableWidget.setObjectName(u"search_tableWidget")
        self.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_3.addWidget(self.search_tableWidget)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(11, 450, 980, 70))
        self.add_pushButton = QPushButton(self.widget_4)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setGeometry(QRect(735, 30, 234, 30))
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
        self.product_label.setGeometry(QRect(250, 30, 235, 30))
        self.product_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.count_comboBox = QComboBox(self.widget_4)
        self.count_comboBox.setObjectName(u"count_comboBox")
        self.count_comboBox.setGeometry(QRect(490, 30, 234, 30))
        self.count_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.user_comboBox = QComboBox(self.widget_4)
        self.user_comboBox.setObjectName(u"user_comboBox")
        self.user_comboBox.setGeometry(QRect(10, 30, 234, 30))
        self.user_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 100, 30))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 0, 120, 30))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 0, 100, 30))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(11, 570, 958, 250))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cart_tableWidget = QTableWidget(self.widget_5)
        self.cart_tableWidget.setObjectName(u"cart_tableWidget")
        self.cart_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_2.addWidget(self.cart_tableWidget)

        self.order_tableWidget = QTableWidget(self.widget_5)
        self.order_tableWidget.setObjectName(u"order_tableWidget")
        self.order_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_2.addWidget(self.order_tableWidget)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(11, 803, 980, 64))
        self.order_pushButton = QPushButton(self.widget_6)
        self.order_pushButton.setObjectName(u"order_pushButton")
        self.order_pushButton.setGeometry(QRect(820, 20, 120, 30))
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
        self.delete_pushButton.setGeometry(QRect(260, 20, 120, 30))
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
        self.delete_label.setGeometry(QRect(140, 20, 100, 30))
        self.delete_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.payment_comboBox = QComboBox(self.widget_6)
        self.payment_comboBox.setObjectName(u"payment_comboBox")
        self.payment_comboBox.setGeometry(QRect(630, 20, 180, 30))
        self.payment_comboBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 60, 60);\n"
"font: 10pt \"Rockwell\"; ")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 120, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 20, 170, 30))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 12pt \"Rockwell\"; ")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 550, 60, 30))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 550, 80, 30))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 130, 171, 30))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"background-color: rgb(0, 0, 0);")

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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Class :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Brand :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Price :", None))
        self.add_pushButton.setText(QCoreApplication.translate("MainWindow", u"Add To Cart", None))
        self.product_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Account :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Product_ID :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Amount :", None))
        self.order_pushButton.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.delete_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Product_ID :</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Payment method : ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cart", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Search Result", None))
    # retranslateUi

