
from datetime import datetime
from DBConnector.DBConnectivity import getDBConn
from models.Customers import Customers
from models.Orders import Orders
from models.Products import Products

class OrderDetails:
    def __init__(self, OrderDetailId, Order: Orders, Product: Products, Quantity):
        self.connection = getDBConn()
        self.OrderDetailId = OrderDetailId
        self.Oders = Order
        self.Product = Product
        self.Quantity = Quantity

    # Getter for OrderDetailId
    def get_OrderDetailId(self):
        return self.OrderDetailId

    # Getter for order
    def get_order(self):
        return self.Oders

    # Getter for Product
    def get_Product(self):
        return self.Product

    # Setter for Product
    def set_Product(self, Product: Products):
        cursor = self.connection.cursor()
        sql = 'UPDATE orderdetails SET ProductID = %s WHERE OrderDetailID = %s'
        para = (Product.get_product_id(), self.OrderDetailId)
        cursor.execute(sql, para)
        self.Product = Product

    # Getter for quantity
    def get_quantity(self):
        return self.Quantity

    # Setter for quantity
    def set_quantity(self, quantity):
        if quantity < 0:
            print('Enter a valid quantity')
            return
        cursor = self.connection.cursor()
        sql = 'UPDATE OrderDetails SET Quantity = %s WHERE OrderDetailID = %s'
        para = (quantity, self.OrderDetailId)
        cursor.execute(sql, para)
        self.Quantity = quantity

    def calculate_subtotal(self):
        return self.Product.get_price() * self.Quantity

    def get_order_detail_info(self):
        details = f"Order Detail ID: {self.OrderDetailId}\n"
        details += f"Order: {self.Oders.get_order_details()}\n"
        details += f"Product: {self.Product.get_product_id()}\n"
        details += f"Quantity: {self.Quantity}\n"
        details += f"Subtotal: ${self.calculate_subtotal():.2f}\n"
        return details

    def update_quantity(self, new_quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE OrderDetails SET Quantity = %s WHERE OrderDetailID = %s'
        para = (new_quantity, self.OrderDetailId)
        cursor.execute(sql, para)
        self.Quantity = new_quantity

    def add_discount(self, discount_percentage):
        discount_factor = 1 - (discount_percentage / 100)
        subtotal = self.calculate_subtotal()
        discounted_subtotal = subtotal * discount_factor
        print(f'Discounted Subtotal {discounted_subtotal}')
