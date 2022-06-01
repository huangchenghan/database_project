from PySide2 import QtGui, QtCore, QtWidgets

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
        
        self.product_attribute = ["Product_ID", "Class", "Brand", "Name", "Price", "Stock", "Release_date", "Recommend", "Is_used", "State"]
        self.product_list = [["A01", "電吉他", "Fender", "墨廠 Classic Player Jaguar Special CAR 電吉他"],
                             ["A02", "木吉他", "gibson", "墨廠 Classic Player Jaguar Special CAR 電吉他"]]
        
        self.user_list = ["ghostlike_上緣", "jokerlike_上緣", "godlike_上緣"]
        
        self.connect_ui()
        
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
            
        self.ui.list_tableWidget.cellClicked.connect(self.tablewidget_click)
    
    def change_brand_combobox(self):
        self.search_class = self.ui.class_comboBox.currentText()
        
        self.ui.brand_comboBox.clear()
        for item in self.class_brand_dict[self.search_class]:
            self.ui.brand_comboBox.addItem(item)
    
    def search_click(self):
        self.search_brand = self.ui.brand_comboBox.currentText() 
        self.search_price = self.ui.price_comboBox.currentText()
        
        if self.ui.secondhand_checkBox.isChecked():
            print("aa")
        if self.ui.recommend_checkBox.isChecked():
            print("bb")
            
        self.list_search_result()
            
    def list_search_result(self):
        self.ui.list_tableWidget.setRowCount(len(self.product_list))
        self.ui.list_tableWidget.setColumnCount(len(self.product_attribute))
        
        self.ui.list_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n" "background-color: rgb(60, 60, 60);")
        self.ui.list_tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
        self.ui.list_tableWidget.verticalHeader().setStyleSheet('QHeaderView::section{color:rgb(255, 255, 255); background:rgb(60, 60, 60);}')
                
        
        self.ui.list_tableWidget.setHorizontalHeaderLabels(self.product_attribute)
        self.ui.list_tableWidget.setVerticalHeaderLabels(["1", "2", "3", "4", "5"])
        
        
        for index in range(self.ui.list_tableWidget.columnCount()):
            headitem=self.ui.list_tableWidget.horizontalHeaderItem(index)
            headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))            
        for index in range(self.ui.list_tableWidget.rowCount()):
            headitem=self.ui.list_tableWidget.verticalHeaderItem(index)
            headitem.setFont(QtGui.QFont("Microsoft JhengHei",10,QtGui.QFont.Bold))
            
        
        for i, product in enumerate(self.product_list):
            for j, attribute in enumerate(product):                
                self.ui.list_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(attribute))
        
    def tablewidget_click(self):
        row_index = self.ui.list_tableWidget.currentRow()
        column_index = self.ui.list_tableWidget.currentColumn()
        self.ui.product_label.setText(self.product_list[row_index][0])
        
    