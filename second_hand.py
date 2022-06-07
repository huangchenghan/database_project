i=80


  self.conn = mysql.connector.connect(host = "localhost",port='3306', user='root', password = 'F74086250', database = 'HIGHLIGHT_musical_instrument_shop')
  self.cursor = self.conn.cursor()

  def insert_click(self):
    self.Product_ID = 'A' + str(i)
    i+=1

    self.Class = '電吉他'
    self.Brand = self.ui.brand_line.text()
    self.Product_name  = self.ui.name_line.text()
    self.Price = -1
    self.Stock = 1
    self.Release_date = '2022-05-01'
    self.recommend = 0
    self.is_used = 1
    self.state = '待審核' + self.ui.contact_line.text()
    
    sql = f"INSERT INTO CART VALUES('{self.Product_ID}', '{self.Class}', '{self.Brand}', '{self.Product_name}', '{self.Price}', '{self.Stock}', '{self.Release_date}', '{self.recommend}', '{self.is_used}', '{self.state}')"
    self.cursor.execute(sql)
    self.conn.commit()