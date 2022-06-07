from errno import ESTALE
from winsound import PlaySound
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import  QMessageBox
from colorama import Cursor
import mysql.connector
import datetime
import time
import pygame

class MainWindow():
    def __init__(self, ui):
        self.ui = ui    
        
        # self.conn = mysql.connector.connect(host = "localhost", user='root', password = 'ddcharles', database = 'HILIGHT_MUSICAL')
        self.conn = mysql.connector.connect(host = "localhost",port='3306', user='root', password = 'F74086250', database = 'HIGHLIGHT_musical_instrument_shop')

        self.cursor = self.conn.cursor()

        self.connect_ui()      
        self.list_search_result()

    def connect_ui(self):        
        self.ui.accept_pushButton.clicked.connect(self.accept_click)   
        self.ui.reject_pushButton.clicked.connect(self.reject_click) 
        
        self.ui.search_tableWidget.cellClicked.connect(self.search_tableWidget_click)
           
    def list_search_result(self):
        self.ui.search_tableWidget.setRowCount(5)
        self.ui.search_tableWidget.setColumnCount(3)
        
        self.ui.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.search_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.search_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        
        self.ui.search_tableWidget.setHorizontalHeaderLabels(["test1", "test2", "test3"])
        self.ui.search_tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])
        
        # for i, product in enumerate(self.product_list):
        #     for j, attribute in enumerate(product):                
        #         self.ui.search_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
           
           
    def search_tableWidget_click(self):
        self.row_index = self.ui.search_tableWidget.currentRow()
        self.column_index = self.ui.search_tableWidget.currentColumn()

        #self.ui.product_label.setText()  
        
        
    def accept_click(self):
        self.product = self.ui.product_label.text()
        self.price = self.ui.price_lineEdit.text()
        self.state = self.ui.state_lineEdit.text()
        
        self.list_search_result()
        
        
    def reject_click(self):
        self.product = self.ui.product_label.text()
        
        self.list_search_result()
        
