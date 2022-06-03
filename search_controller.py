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
        self.is_birthday=0
        self.ui = ui    
        self.class_list = ["不限", "木吉他", "電吉他", "貝斯", "MIDI鍵盤"]
        self.brand_list = ["不限", "Cort", "Fender", "gibson", "Bacchus", "Novation"]
        self.price_list = ["不限", "0~10000", "10000~20000", "20000~30000"]
        
        self.search_class = "不限"
        self.search_brand = "不限"
        self.search_price = "不限"
        
        self.class_brand_dict = {"不限":["不限", "Cort", "Fender", "gibson", "Bacchus", "Novation"], "木吉他":["不限", "Cort"], "電吉他":["不限", "Fender", "gibson"],
                                 "貝斯":["不限", "Bacchus"], "MIDI鍵盤":["不限", "Novation"]}
        
        self.product_attribute = ["Product_ID", "Class", "Brand", "Name", "Price", "Stock", "Release_date",  "State","audition"]
        self.product_list = [["A01", "電吉他", "Fender", "墨廠 Classic Player Jaguar Special CAR 電吉他"],
                             ["A02", "木吉他", "gibson", "墨廠 Classic Player Jaguar Special CAR 電吉他"]]
        
        self.cart_attribute = ["Account", "Product_ID", "Amount"]
        self.order_attribute = ["訂單編號", "商品編號","商品類別","商品品牌","商品名稱","單價","購買數量", "送貨地址","訂單成立時間","發貨狀態","付款方式","是否付款","附註"]
        self.cart_list = [["charles", "A01", "2"],
                          ["shang", "A02", "2"]]
        
        self.payment_list = ["信用卡", "匯款", "貨到付款"]
        
        # self.user_list = ["charles", "shang", "wx200010"]
        # self.conn = mysql.connector.connect(host = "localhost", user='root', password = 'ddcharles', database = 'HILIGHT_MUSICAL')
        self.user_list = ["F74084737","F74086250"]
        self.conn = mysql.connector.connect(host = "localhost",port='3306', user='root', password = 'F74086250', database = 'HIGHLIGHT_musical_instrument_shop')


        self.cart_order = 0

        self.cursor = self.conn.cursor()
        self.replenishment()
        self.connect_ui()
        self.list_cart_result()
        self.list_order_result()

    def replenishment(self):
        replenishment_sql_command=f"UPDATE PRODUCT SET STOCK = 10 WHERE Product_ID = 'A01'"
        self.cursor.execute(replenishment_sql_command)
        self.conn.commit()
        replenishment_sql_command=f"UPDATE PRODUCT SET STOCK = 10 WHERE Product_ID = 'A02'"
        self.cursor.execute(replenishment_sql_command)
        self.conn.commit()


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
        
        self.ui.add_pushButton.clicked.connect(self.add_click)
        
        self.ui.cart_tableWidget.cellClicked.connect(self.cart_tablewidget_click)
        
        #self.ui.order_tableWidget.cellClicked.connect(self.order_tablewidget_click)

        self.ui.delete_pushButton.clicked.connect(self.delete_click)
        
        for item in self.payment_list:
            self.ui.payment_comboBox.addItem(item) 
        
        self.ui.order_pushButton.clicked.connect(self.order_click)

        self.ui.user_comboBox.currentIndexChanged.connect(self.list_result)

    def change_brand_combobox(self):
        self.search_class = self.ui.class_comboBox.currentText()
        
        self.ui.brand_comboBox.clear()
        for item in self.class_brand_dict[self.search_class]:
            self.ui.brand_comboBox.addItem(item)
            

    def search_click(self):
        self.search_brand = self.ui.brand_comboBox.currentText() 
        self.search_price = self.ui.price_comboBox.currentText()
        # print(self.useraccount)
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
            del self.product_list[i][7:9]
        #print(self.product_list)
        #print(self.useraccount)
        self.conn.commit()
        loc_dt = datetime.datetime.today() 
        loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
        loc_dt_format=loc_dt_format.split("/")
        select_birthday_sql_command=f"select Birthday from CUSTOMER WHERE Customer_account='{self.useraccount}'"
        self.cursor.execute(select_birthday_sql_command)
        birthday_list=[]
        records=self.cursor.fetchall()
        for r in records:
            birthday_list.append(list(r))
        birthday=str(birthday_list[0])
        birthday=birthday.split(",")
        print(self.useraccount)
        if int(birthday[1])==int(loc_dt_format[1]):
            self.is_birthday=1
            for i in range(len(self.product_list)):
                self.product_list[i][4]=str(round(int(self.product_list[i][4])*0.9))
        else:
            self.is_birthday=0
        #print(self.product_list)

        
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
        self.row_index_product = self.ui.search_tableWidget.currentRow()
        self.column_index_product = self.ui.search_tableWidget.currentColumn()
        self.ui.product_label.setText(self.product_list[self.row_index_product][0])
        Isplay = True
        if(self.column_index_product == 8):
            pygame.mixer.init()
            if(self.product_list[self.row_index_product][8] != ""):
                pygame.mixer.music.load(self.product_list[self.row_index_product][8])
                pygame.mixer.music.play()

        
        self.count = self.product_list[self.row_index_product][5]
        self.ui.count_comboBox.clear()
        for i in range(int(self.count)):
            self.ui.count_comboBox.addItem(str(i+1))
        
    
    def add_click(self):
        self.useraccount = self.ui.user_comboBox.currentText()
        self.productID = self.product_list[self.row_index_product][0]
        self.count = self.ui.count_comboBox.currentText()

        sql = f"INSERT INTO CART VALUES('{self.useraccount}', '{self.productID}',{self.count})"
        self.cursor.execute(sql)
        self.conn.commit()
        self.list_cart_result()
            
    def get_cart(self):
        self.useraccount = self.ui.user_comboBox.currentText()
        sql = f"SELECT * FROM CART WHERE Customer_account = '{self.useraccount}'"
        self.cursor.execute(sql)
        carts = self.cursor.fetchall()
        self.cart_list = []
        for i in range(len(carts)):
            self.cart_list.append(list(carts[i]))
            for j in range(len(self.cart_list[-1])):
                self.cart_list[-1][j] = str(self.cart_list[-1][j])
    def get_order(self):
        self.useraccount = self.ui.user_comboBox.currentText()
        sql = f"SELECT OO.OrderNo,P.Product_ID,P.Class,P.Brand,P.Product_name,P.Price,OO.Amount,OI.Address,OI.Established_date,OI.State,OI.PaymentMethod,OI.IsPaid,OO.Note FROM ORDER_INFO AS OI,ORDER_OUTLINE AS OO,PRODUCT AS P WHERE OO.Product_id=P.Product_ID and OO.OrderNo=OI.OrderNo and OI.Customer_account='{self.useraccount}';"
        self.cursor.execute(sql)
        carts = self.cursor.fetchall()
        self.order_list = []
        for i in range(len(carts)):
            self.order_list.append(list(carts[i]))
            for j in range(len(self.order_list[-1])):
                self.order_list[-1][j] = str(self.order_list[-1][j])

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
    def list_result(self):
        self.useraccount=self.ui.user_comboBox.currentText()
        self.search_click()
        self.list_cart_result()
        self.list_order_result()
    def list_order_result(self):
        self.get_order()
        self.ui.order_tableWidget.setRowCount(len(self.order_list))
        self.ui.order_tableWidget.setColumnCount(len(self.order_attribute))
        
        self.ui.order_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.order_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.order_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        
        self.ui.order_tableWidget.setHorizontalHeaderLabels(self.order_attribute)
        self.ui.order_tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])
        
        for index in range(self.ui.order_tableWidget.columnCount()):
            headitem=self.ui.order_tableWidget.horizontalHeaderItem(index)
          #  headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))            
        for index in range(self.ui.order_tableWidget.rowCount()):
            headitem=self.ui.order_tableWidget.verticalHeaderItem(index)
           # headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))
            
        for i, cart in enumerate(self.order_list):
            for j, attribute in enumerate(cart):                
                self.ui.order_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
        
    def cart_tablewidget_click(self):
        self.row_index_cart = self.ui.cart_tableWidget.currentRow()
        self.column_index_cart = self.ui.cart_tableWidget.currentColumn()
        self.ui.delete_label.setText(self.cart_list[self.row_index_cart][1])
    # def order_tablewidget_click(self):
    #     self.row_index_order = self.ui.order_tableWidget.currentRow()
    #     self.column_index_order = self.ui.order_tableWidget.currentColumn()
    #     self.ui.delete_label.setText(self.order_list[self.row_index_order][0])    

        
    def delete_click(self):
        delete_cart_sql_command=f"delete from cart where Customer_account='{self.useraccount}' and Product_id='{self.cart_list[self.row_index_cart][1]}'"
        self.cursor.execute(delete_cart_sql_command)
        self.conn.commit()
        self.list_result()
    # del delete_click_order(self):


        
    
    def order_click(self):
        select_from_cart_command=f"select * from cart WHERE Customer_account = '{self.useraccount}';"
        self.cursor.execute(select_from_cart_command)
        # 取出該用戶的購物車資料
        self.cart_convert_into_order_list=[]
        records=self.cursor.fetchall()
        for r in records:
            self.cart_convert_into_order_list.append(list(r))
        # 檢查購物車中是否有商品數量超過庫存
        Exceed_Stock = False
        for i in range(len(self.cart_convert_into_order_list)):
            Product_id = self.cart_convert_into_order_list[i][1]
            Amount = self.cart_convert_into_order_list[i][2]
            select_command=f"SELECT STOCK FROM PRODUCT WHERE Product_id = '{Product_id}' "
            self.cursor.execute(select_command)
            records=self.cursor.fetchall()
            STOCK=int(list(records[0])[0])
            # 若有任一商品超過庫存，則報錯，拒絕訂單成立
            if(Amount > STOCK):
                Exceed_Stock = True
                print(f"編號{Product_id}的商品已超過庫存{STOCK}")
                break
        # 若商品數量皆不超過庫存，則代表該訂單可以成立：
        if(Exceed_Stock == False):

            Serial_no=0
            # 開始插入 Order_info 
            loc_dt = datetime.datetime.today() 
            loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
            self.OrderNo=self.useraccount+"_"+loc_dt_format
            Serial_no+=1
            self.cursor.execute(f"select Address from CUSTOMER WHERE Customer_account = '{self.useraccount}';")
            records=self.cursor.fetchall()
            Address=list(records[0])[0]

            Established_date=str(datetime.date.today())
            completion_date=str(datetime.date.today())
            State="訂單準備中"
            PaymentMethod="信用卡"
            IsPaid="0"
            insert_command='INSERT INTO '+ 'ORDER_INFO'+' VALUES'+f"('{self.OrderNo}','{self.useraccount}','{Address}','{Established_date}','{completion_date}','{State}','{PaymentMethod}','{IsPaid}');"
            self.cursor.execute(insert_command)
            self.conn.commit()

        # 開始對每件商品插入 ORDER
        for i in range(len(self.cart_convert_into_order_list)): #Customer_account,Product_id,Amount
            Product_id = self.cart_convert_into_order_list[i][1]
            Amount = self.cart_convert_into_order_list[i][2]
            Note = "no"
            insert_command='INSERT INTO '+'ORDER_OUTLINE'+' VALUES '+f"('{self.OrderNo}','{Product_id}','{Amount}','{Note}');"
            self.cursor.execute(insert_command)
            self.conn.commit()
            # 開始更新商品庫存

            # 取得目前商品的STOCK
            select_command=f"SELECT STOCK FROM PRODUCT WHERE Product_id = '{Product_id}' "
            self.cursor.execute(select_command)
            records=self.cursor.fetchall()
            STOCK=int(list(records[0])[0])

            # 減少商品庫存
            update_command=f"UPDATE PRODUCT SET STOCK = {STOCK-Amount} WHERE Product_ID = '{Product_id}'"
            self.cursor.execute(update_command)
            self.conn.commit()

        # 清空該用戶的購物車資料
        delete_command = f"DELETE FROM CART WHERE Customer_account = '{self.useraccount}';"
        self.cursor.execute(delete_command)
        self.conn.commit()
        self.list_cart_result()
        self.search_click()
        self.custom_message()
        self.list_order_result()

    def custom_message(self):
        msg_box = QMessageBox(self)
        # msg_box.setIcon(QMessageBox.Question)
        # msg_box.setStandardButtons(QMessageBox.Yes)
        # msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle('Order Information')
        select_order_info_sql_command=f"select established_date,State,PaymentMethod from ORDER_INFO where OrderNo='{self.OrderNo}';"
        #print(select_order_info_sql_command)
        self.cursor.execute(select_order_info_sql_command)
        order_list=[]
        records=self.cursor.fetchall()
        for r in records:
            order_list.append(list(r))
        msg_box.setText(f"Order Number:\t\t{self.OrderNo}\nEstablished Date:\t{str(order_list[0][0])}\nState:\t\t\t\t{order_list[0][1]}\nPayment Method:\t{order_list[0][2]}\n")

        
        select_order_outline_sql_command=f"select OO.Product_id,P.Product_name,P.Price,OO.Amount from PRODUCT AS P,ORDER_OUTLINE AS OO where OO.OrderNO='{self.OrderNo}' and OO.Product_id=P.Product_ID;"
        self.cursor.execute(select_order_outline_sql_command)
        order_product_list=[]
        records=self.cursor.fetchall()
        for r in records:
            order_product_list.append(list(r))
       
        # msg_box.setInformativeText(f'Established Date:\t{str(order_list[0][0])}\nState:\t\t\t\t{order_list[0][1]}\nPayment Method:\t{order_list[0][2]}\n')
        total_money=0
        for i in range(len(order_product_list)):
            total_money+=(order_product_list[i][2]*order_product_list[i][3])
        postfix_happybirthday_string=""
        if(self.is_birthday==1):
            total_money=round(total_money*0.9)
            postfix_happybirthday_string="Happy Birthday!You have a 10% off discount!\n"

        if(len(order_product_list)==1):
            msg_box.setInformativeText(f'{order_product_list[0][0]},{order_product_list[0][1]},{order_product_list[0][2]},{order_product_list[0][3]}\n\n\n{postfix_happybirthday_string}總金額:{total_money}\n')
        else:
            msg_box.setInformativeText(f'{order_product_list[0][0]},{order_product_list[0][1]},{order_product_list[0][2]},{order_product_list[0][3]}\n{order_product_list[1][0]},{order_product_list[1][1]},{order_product_list[1][2]},{order_product_list[1][3]}\n\n\n{postfix_happybirthday_string}總金額:{total_money}\n')
         

            
        # msg_box.setDetailedText(
        #     'Follow our Bucketing page, and learn more'
        #     'about PySide2, Java, Design pattern!\n'
        #     'Enjoy!')
        # msg_box.setStyleSheet("min-width:1000 px;min-height:100 px; font-size: 24px; font-size:30px; background-color: rgb(0,0,0);color: rgb(255,255,255);")
        msg_box.setStyleSheet("QLabel{min-width:1000 px;min-height:100 px; font-size: 24px; font-size:30px; background-color: rgb(0,0,0);color: rgb(255,255,255);} QPushButton{ width:250px; font-size: 18px;background-color: Silver;}")
        msg_box.addButton('OK',QMessageBox.AcceptRole)
        msg_box.show()
