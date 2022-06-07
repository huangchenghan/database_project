
    def search_click(self):
        
        self.product_list = []
        sql = f"SELECT * FROM PRODUCT WHERE Price = -1"
        
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
        print(birthday_list)
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
        