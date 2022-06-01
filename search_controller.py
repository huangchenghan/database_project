from errno import ESTALE
from PySide2 import QtGui, QtCore, QtWidgets
from colorama import Cursor
import mysql.connector

class MainWindow():
    def __init__(self, ui):
        self.ui = ui    
        self.class_list = ["不限", "木吉他", "電吉他", "貝斯", "MIDI鍵盤"]
        self.brand_list = ["不限", "Cort", "Fender", "gibson", "Bacchus", "Novation"]
        self.price_list = ["不限", "0~10000", "10000~20000", "20000~30000"]
        
        self.search_class = "不限"
        self.search_brand = "不限"
        self.search_price = "不限"
        
        self.class_brand_dict = {"不限":["不限", "Cort", "Fender", "gibson", "Bacchus", "Novation"], "木吉他":["不限", "Cort"], "電吉他":["不限", "Fender", "gibson"],
                                 "貝斯":["不限", "Bacchus"], "MIDI鍵盤":["不限", "Novation"]}
        
        self.product_attribute = ["Product_ID", "Class", "Brand", "Name", "Price", "Stock", "Release_date",  "State"]
        self.product_list = [["A01", "電吉他", "Fender", "墨廠 Classic Player Jaguar Special CAR 電吉他"],
                             ["A02", "木吉他", "gibson", "墨廠 Classic Player Jaguar Special CAR 電吉他"]]
        
        self.cart_attribute = ["Account", "Product_ID", "Amount"]
        self.cart_list = [["charles", "A01", "2"],
                          ["shang", "A02", "2"]]
        
        self.user_list = ["charles", "shang", "wx200010"]
        self.conn = mysql.connector.connect(host = "localhost", user='root', password = 'ddcharles', database = 'HILIGHT_MUSICAL')

        self.cursor = self.conn.cursor()
        self.connect_ui()
        self.list_cart_result()
        
    def connect_ui(self):
        for item in self.class_list:
            self.ui.class_comboBox.addItem(item)
        self.ui.class_comboBox.currentIndexChanged.connect(self.change_brand_combobox)
            
        for item in self.brand_list:
            self.ui.brand_comboBox.addItem(item)
            
        for item in self.price_list:
            self.ui.price_comboBox.addItem(item)
        
        self.ui.search_pushButton.clicked.connect(self.search_click)      
        
        for item in self.user_list:
            self.ui.user_comboBox.addItem(item) 
            
        self.ui.search_tableWidget.cellClicked.connect(self.search_tableWidget_click)
        
        self.ui.add_pushButton.clicked.connect(self.add_cart)
        
        self.ui.cart_tableWidget.cellClicked.connect(self.cart_tablewidget_click)
        
        self.ui.delete_pushButton.clicked.connect(self.delete_click)
        
        self.ui.order_pushButton.clicked.connect(self.order_click)

        self.ui.user_comboBox.currentIndexChanged.connect(self.list_cart_result)

    def change_brand_combobox(self):
        self.search_class = self.ui.class_comboBox.currentText()
        
        self.ui.brand_comboBox.clear()
        for item in self.class_brand_dict[self.search_class]:
            self.ui.brand_comboBox.addItem(item)
    
    def get_cart(self):
        account = self.ui.user_comboBox.currentText()
        sql = f"SELECT * FROM CART WHERE Customer_account = '{account}'"
        self.cursor.execute(sql)
        carts = self.cursor.fetchall()
        self.cart_list = []
        for i in range(len(carts)):
            self.cart_list.append(list(carts[i]))
            for j in range(len(self.cart_list[-1])):
                self.cart_list[-1][j] = str(self.cart_list[-1][j])
            

    def search_click(self):
        self.search_brand = self.ui.brand_comboBox.currentText() 
        self.search_price = self.ui.price_comboBox.currentText()
        
        if self.ui.secondhand_checkBox.isChecked():
            self.IsSecond_hand = True
        #    print("aa")
        else:
            self.IsSecond_hand = False
        if self.ui.recommend_checkBox.isChecked():
            self.IsRecommend = True
         #   print("bb")
        else:
            self.IsRecommend = False
        self.product_list = []
        sql = f"SELECT * FROM PRODUCT "
        sql2 = ""
        if(self.IsSecond_hand):
            sql2 += f"AND is_used = {self.IsSecond_hand} "
        if(self.IsRecommend):
            sql2 += f"AND recommend = {self.IsRecommend} "
        if(self.search_brand != "不限"):
            sql2 += f"AND Brand = '{self.search_brand}' "
        if (self.search_class != "不限") :
            sql2 += f"AND Class = '{self.search_class}' "
        if( self.search_price != "不限"):
            price = self.search_price.split("~")
            sql2 += f"AND {price[0]} <= Price AND Price <{price[1]} "
        if(sql2 != ""):
            sql = sql + "WHERE" +sql2[3:]
        #print(sql)
        self.cursor.execute(sql)
        products = self.cursor.fetchall()
        for i in range(len(products)):
            # self.product_list.append(list(products[i]))
            #print(list(products[i]))
            self.product_list.append(list(products[i]))
            for j in range(len(self.product_list[i])):
                self.product_list[i][j] = str(self.product_list[i][j])
            del self.product_list[i][-2]
            del self.product_list[i][-2]
        #print(self.product_list)
        self.conn.commit()
        
        self.list_search_result()
            
    def list_search_result(self):
        self.ui.search_tableWidget.setRowCount(len(self.product_list))
        self.ui.search_tableWidget.setColumnCount(len(self.product_attribute))
        
        self.ui.search_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.search_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.search_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
                
        
        self.ui.search_tableWidget.setHorizontalHeaderLabels(self.product_attribute)
        self.ui.search_tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])
        
        
        for index in range(self.ui.search_tableWidget.columnCount()):
            headitem=self.ui.search_tableWidget.horizontalHeaderItem(index)
           # headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))            
        for index in range(self.ui.search_tableWidget.rowCount()):
            headitem=self.ui.search_tableWidget.verticalHeaderItem(index)
            #headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))
            
        
        for i, product in enumerate(self.product_list):
            for j, attribute in enumerate(product):                
                self.ui.search_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
        
    def search_tableWidget_click(self):
        self.row_index = self.ui.search_tableWidget.currentRow()
        self.column_index = self.ui.search_tableWidget.currentColumn()
        self.ui.product_label.setText(self.product_list[self.row_index][0])
        
        self.count = self.product_list[self.row_index][5]
        self.ui.count_comboBox.clear()
        for i in range(int(self.count)):
            self.ui.count_comboBox.addItem(str(i+1))
        
    
    def add_cart(self):
        self.useraccount = self.ui.user_comboBox.currentText()
        self.productID = self.product_list[self.row_index][0]
        self.count = self.ui.count_comboBox.currentText()

        sql = f"INSERT INTO CART VALUES('{self.useraccount}', '{self.productID}',{self.count})"
        self.cursor.execute(sql)
        self.conn.commit()
        self.list_cart_result()
    
    def list_cart_result(self):
        self.get_cart()
        self.ui.cart_tableWidget.setRowCount(len(self.cart_list))
        self.ui.cart_tableWidget.setColumnCount(len(self.cart_attribute))
        
        self.ui.cart_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.cart_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.cart_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        
        self.ui.cart_tableWidget.setHorizontalHeaderLabels(self.cart_attribute)
        self.ui.cart_tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])
        
        for index in range(self.ui.cart_tableWidget.columnCount()):
            headitem=self.ui.cart_tableWidget.horizontalHeaderItem(index)
          #  headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))            
        for index in range(self.ui.cart_tableWidget.rowCount()):
            headitem=self.ui.cart_tableWidget.verticalHeaderItem(index)
           # headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))
            
        for i, cart in enumerate(self.cart_list):
            for j, attribute in enumerate(cart):                
                self.ui.cart_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
        
    def cart_tablewidget_click(self):
        self.row_index = self.ui.cart_tableWidget.currentRow()
        self.column_index = self.ui.cart_tableWidget.currentColumn()
        self.ui.product_label.setText(self.cart_list[self.row_index][1])
        
    def delete_click(self):
        pass
    
    def order_click(self):
        pass