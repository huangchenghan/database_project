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

    def connect_ui(self):        
        self.ui.send_pushButton.clicked.connect(self.send_click)      
        
    def send_click(self):
        self.brand = self.ui.brand_lineEdit.text()
        self.name = self.ui.name_lineEdit.text()
        self.contact = self.ui.contact_lineEdit.text()
