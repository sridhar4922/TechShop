from datetime import datetime
from models.Customers import Customers
from DBConnector.DBConnectivity import getDBConn

class Orders:
    def __init__(self, order_id, customer: Customers, order_date, total_amount, order_status="Pending"):
        self.connection = getDBConn()
        self.OrderId = order_id
        self.Customer = customer
        self.OrderDate = order_date
        self.TotalAmount = total_amount
        self.OrderStatus = order_status

    # Getter for order_id
    def get_order_id(self):
        return self.OrderId

    # Getter for customer
    def get_customer(self):
        return self.Customer

    # Getter for order_date
    def get_order_date(self):
        return self.OrderDate

    # Setter for order_date
    def set_order_date(self, order_date):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET OrderDate = %s WHERE OrderID = %s'
        para = (order_date, self.OrderId)
        cursor.execute(sql, para)
        self.OrderDate = order_date

    # Getter for total_amount
    def get_total_amount(self):
        return self.TotalAmount

    # Setter for total_amount
    def set_total_amount(self, total_amount):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s'
        para = (total_amount, self.OrderId)
        cursor.execute(sql, para)
        self.TotalAmount = total_amount

    # Getter for order_status
    def get_order_status(self):
        return self.OrderStatus

    # Setter for order_status
    def set_order_status(self, order_status):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET OrderStatus= %s WHERE OrderID = %s'
        para = (order_status, self.OrderId)
        cursor.execute(sql, para)
        self.OrderStatus = order_status

    def calculate_total_amount(self):
        cursor = self.connection.cursor()
        sql = 'SELECT SUM(OrderDetails.Quantity*orders.TotalAmount) AS TotalAmount FROM OrderDetails JOIN Orders on OrderDetails.OrderID = orders.OrderID WHERE orders.OrderID = %s'
        para = (self.OrderId)
        cursor.execute(sql, para)
        TotalAmount = list(cursor.fetchone())[0]
        return TotalAmount

    def get_order_details(self):
        details = f"Order ID: {self.OrderId}\n"
        details += f"Customer: {self.Customer.get_customer_details()}\n"
        details += f"Order Date: {self.OrderDate}\n"
        details += f"Total Amount: ${self.calculate_total_amount():.2f}\n"
        details += f"Order Status: {self.OrderStatus}\n"
        return details

    def update_order_status(self, new_status):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET OrderStatus= %s WHERE OrderID = %s'
        para = (new_status, self.OrderId)
        cursor.execute(sql, para)
        self.OrderStatus = new_status

    def cancel_order(self):
        cursor = self.connection.cursor()
        sql = 'UPDATE Orders SET OrderStatus= %s WHERE OrderID = %s'
        para = ('Cancelled', self.OrderId)
        cursor.execute(sql, para)
        self.OrderStatus = "Cancelled"
        print('Order successfully cancelled')