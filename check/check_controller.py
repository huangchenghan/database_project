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
        
        self.conn = mysql.connector.connect(host = "localhost", user='root', password = 'ddcharles', database = 'HILIGHT_MUSICAL')
        # self.conn = mysql.connector.connect(host = "localhost",port='3306', user='root', password = 'F74086250', database = 'HIGHLIGHT_musical_instrument_shop')
        classes = ["電吉他","木吉他","貝斯","MIDI鍵盤","其他"]
        for i in range(len(classes)):
            self.ui.class_comboBox.addItem(classes[i])
        self.cursor = self.conn.cursor()

        self.connect_ui()      
        self.search_click()

    def search_click(self):
        
        self.product_list = []
        sql = f"SELECT Product_ID,Product_name,State FROM PRODUCT WHERE Price = -1"
        
        #print(sql)
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        for i in range(len(products)):
            # self.product_list.append(list(products[i]))
            #print(list(products[i]))
            self.product_list.append(list(products[i]))
            for j in range(len(self.product_list[i])):
                self.product_list[i][j] = str(self.product_list[i][j])
        #print(self.product_list)
        #print(self.useraccount)
        self.conn.commit()
        # loc_dt = datetime.datetime.today() 
        # loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
        # loc_dt_format=loc_dt_format.split("/")
        # select_birthday_sql_command=f"select Birthday from CUSTOMER WHERE Customer_account='{self.useraccount}'"
        # self.cursor.execute(select_birthday_sql_command)
        # birthday_list=[]
        # records=self.cursor.fetchall()
        # for r in records:
        #     birthday_list.append(list(r))
        # print(birthday_list)
        # birthday=str(birthday_list[0])
        # birthday=birthday.split(",")
        # print(self.useraccount)
        # if int(birthday[1])==int(loc_dt_format[1]):
        #     self.is_birthday=1
        #     for i in range(len(self.product_list)):
        #         self.product_list[i][4]=str(round(int(self.product_list[i][4])*0.9))
        # else:
        #     self.is_birthday=0
        # #print(self.product_list)
    
        self.list_search_result()
    def connect_ui(self):        
        self.ui.accept_pushButton.clicked.connect(self.accept_click)   
        self.ui.reject_pushButton.clicked.connect(self.reject_click) 
        
        self.ui.search_tableWidget.cellClicked.connect(self.search_tableWidget_click)
           
    def list_search_result(self):
        self.ui.search_tableWidget.setRowCount(len(self.product_list))
        self.ui.search_tableWidget.setColumnCount(3)
        
        self.ui.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.search_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.search_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        
        self.ui.search_tableWidget.setHorizontalHeaderLabels(["Product_ID", "Product_name", "Contact_info"])
        self.ui.search_tableWidget.setVerticalHeaderLabels([x for x in range(len(self.product_list))])
        
        for i, product in enumerate(self.product_list):
            for j, attribute in enumerate(product):                
                self.ui.search_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
           
           
    def search_tableWidget_click(self):
        self.row_index = self.ui.search_tableWidget.currentRow()
        self.column_index = self.ui.search_tableWidget.currentColumn()
        self.ui.product_label.setText(self.product_list[self.row_index][0])
        #self.ui.product_label.setText()  
        
        
    def accept_click(self):
        self.product = self.ui.product_label.text()
        self.price = self.ui.price_lineEdit.text()
        self.state = self.ui.state_lineEdit.text()
        self.classes = self.ui.class_comboBox.currentText()
        #print(self.product,self.price,self.state)
        
        update_sql=f"update PRODUCT set Price = {self.price},state='{self.state}',Class ='{self.classes}' where Product_ID ='{self.product}'"
        self.cursor.execute(update_sql)
        self.conn.commit()
        self.ui.price_lineEdit.setText("")
        self.ui.product_label.setText("")
        self.ui.state_lineEdit.setText("")
        self.search_click()
        
        
    def reject_click(self):
        self.product = self.ui.product_label.text()
        delete_sql=f"delete from PRODUCT where Product_ID='{self.product}'"
        self.cursor.execute(delete_sql)
        self.conn.commit()
        self.ui.price_lineEdit.setText("")
        self.ui.product_label.setText("")
        self.ui.state_lineEdit.setText("")
        self.search_click()
        
