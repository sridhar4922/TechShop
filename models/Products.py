
from DBConnector.DBConnectivity import getDBConn

class Products:
    def __init__(self, ProductId, ProductName, Description, Price):
        self.connection = getDBConn()
        self.ProductId = ProductId
        self.ProductName = ProductName
        self.Description = Description
        self.Price = Price

    def get_ProductId(self):
        return self.ProductId

    def set_ProductId(self, ProductId):
        sql = 'UPDATE Products SET ProductId = %s WHERE ProductId = %s'
        para = (ProductId, self.ProductId)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.ProductId = ProductId

    def get_ProductName(self):
        return self.ProductName

    def set_ProductName(self, ProductName):
        sql = 'UPDATE Products SET ProductName = %s WHERE ProductId = %s'
        para = (ProductName, self.ProductId)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.ProductName = ProductName

    def get_Description(self):
        return self.Description

    def set_Description(self, Description):
        sql = 'UPDATE Products SET Description = %s WHERE ProductID = %s'
        para = (Description, self.ProductId)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.Description = Description

    def get_Price(self):
        return self.Price

    def set_Price(self, Price):
        sql = 'UPDATE Products SET Price = %s WHERE productID = %s'
        para = (Price, self.ProductId)
        cursor = self.connection.cursor()
        cursor.execute(sql, para)
        self.Price = Price

    def get_product_details(self):
        details = f"Product ID: {self.ProductId}\n"
        details += f"Product Name: {self.ProductName}\n"
        details += f"Description: {self.Description}\n"
        details += f"Price: ${self.Price:.2f}\n"
        return details

    def update_product_info(self, Price=None, Description=None):
        if Price:
            cursor = self.connection.cursor()
            sql = 'UPDATE Products SET Price = %s WHERE ProductID = %s'
            para = (Price, self.ProductId)
            cursor.execute(sql, para)
            self.Price = Price
        if Description:
            cursor = self.connection.cursor()
            sql = 'UPDATE Products SET Description = %s WHERE ProductID = %s'
            para = (Description, self.ProductId)
            cursor.execute(sql, para)
            self.Description = Description

    def is_product_in_stock(self):
        cursor = self.connection.cursor()
        sql = 'SELECT Inventory.QuantityInStock FROM Products JOIN Inventory ON Products.ProductID = Inventory.ProductID WHERE Products.ProductID = %s'
        para = (self.ProductId,)
        cursor.execute(sql, para)
        x = list(cursor.fetchone())[0]
        return x > 0
