from errno import ESTALE
from random import randrange
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
        self.i=81
        self.conn = mysql.connector.connect(host = "localhost", user='root', password = 'ddcharles', database = 'HILIGHT_MUSICAL')
        # self.conn = mysql.connector.connect(host = "localhost",port='3306', user='root', password = 'F74086250', database = 'HIGHLIGHT_musical_instrument_shop')
        self.cursor = self.conn.cursor()

        self.connect_ui()

    def connect_ui(self):        
        self.ui.send_pushButton.clicked.connect(self.send_click)      
        
    def send_click(self):    
        sql = "SELECT Product_ID FROM PRODUCT WHERE Product_ID LIKE \'Z%\'"
        self.cursor.execute(sql)
        num = self.cursor.fetchall()
        print(num[0])
        for i in range(len(num)):
            if('Z' + str(i) != num[i][0]):
                self.Product_ID = 'Z' + str(i)
                break
            if i == len(num)-1:
                self.Product_ID = 'Z' + str(i+1)
                
        
        
        self.Brand = self.ui.brand_lineEdit.text()
        self.Product_name = self.ui.name_lineEdit.text()
        self.Class = '電吉他'
        self.Price = -1
        self.Stock = 1
        loc_dt = datetime.datetime.today() 
        loc_dt_format = loc_dt.strftime("%Y/%m/%d")
        self.Release_date = loc_dt_format
        self.recommend = 0
        self.is_used = 1
        self.state = '待審核' + self.ui.contact_lineEdit.text()
        
        sql = f"INSERT INTO PRODUCT VALUES('{self.Product_ID}', '{self.Class}', '{self.Brand}', '{self.Product_name}', '{self.Price}', '{self.Stock}', '{self.Release_date}', '{self.recommend}', '{self.is_used}', '{self.state}','')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.ui.name_lineEdit.setText("")  #set text null
        self.ui.brand_lineEdit.setText("") #set text null
        self.ui.contact_lineEdit.setText("")