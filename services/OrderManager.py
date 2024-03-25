from datetime import datetime

from custom_exception.CustomException import OrderNotFoundException
from models.Orders import Orders
from models.Products import Products
from DBConnector.DBConnectivity import getDBConn

def getAllOrders() -> list:
    mydb = getDBConn()
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Orders'
    mycursor.execute(sql)
    t = list(mycursor.fetchall())
    x = []
    for i in t: x.append(list(i))
    return x

class OrderManager:
    def __init__(self):
        self.connection = getDBConn()

    def add_order(self, order: Orders):
        try:
            mycursor = self.connection.cursor()
            sql = 'INSERT INTO Orders(OrderID, CustomerID, OrderDate, TotalAmount, OrderStatus) VALUES (%s, %s, %s, %s, %s, %s)'
            para = (order.get_order_id(), order.get_customer().get_customer_id(), order.get_order_date(), order.get_total_amount(), order.get_order_status())
            mycursor.execute(sql, para)
            self.connection.commit()
            print(f"Order {order.get_order_id()} added successfully.")
        except Exception as e:
            print(f"Error adding order: {e}")

    def update_order_status(self, order_id, new_status):
        try:
            mycursor = self.connection.cursor()
            sql = 'UPDATE Order SET OrderStatus = %s WHERE OrderID = %s'
            para = (new_status, order_id)
            mycursor.execute(sql, para)
            self.connection.commit()
        except Exception as e:
            print(f"Error updating order status: {e}")

    def remove_canceled_orders(self):
        try:
            mycursor = self.connection.cursor()
            sql1 = '''DELETE FROM OrderDetails WHERE OrderID IN
                    (SELECT OrderID FROM Orders WHERE OrderStatus IN ('Cancelled', 'cancelled')'''
            sql2 = '''DELETE FROM Orders WHERE OrderStatus IN ('Cancelled', 'cancelled')'''
            mycursor.execute(sql1)
            mycursor.execute(sql2)
            print(f"Orders removed successfully")
        except Exception as e:
            print(f"Error removing canceled orders: {e}")

    def sort_orders_by_date(self, ascending=True):
        mydb = getDBConn()
        mycursor = mydb.cursor()
        sql = 'SELECT * FROM Orders ORDER BY OrderDate ASC'
        mycursor.execute(sql)
        t = list(mycursor.fetchall())
        x = []
        for i in t:
            x.append(list(i))
        if not ascending:
            x.reverse()
        return x

    def list_all_orders(self):
        return getAllOrders()

    def get_order_by_id(self, order_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Orders WHERE orderID = %s'''
            para = (order_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise OrderNotFoundException('Invalid Order ID')
            else:
                return Orders(*x)
        except OrderNotFoundException as onfe:
            print('An error occurred ',onfe)
        except Exception as e:
            print('An error occurred ',e)