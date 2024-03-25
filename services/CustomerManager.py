
import re
from custom_exception.CustomException import CustomerNotFoundException
from models.Customers import Customers
from DBConnector.DBConnectivity import getDBConn
class CustomerManager:
    def __init__(self):
        self.connection = getDBConn()

    def register_customer(self, FirstName, LastName, Email, DateOfBirth, Phone, NumOrders, Address):
        try:
            # Validating input data
            self.validate_customer_data(Email)
            # Checking if the Email already exists in the database
            if self.is_Email_duplicate(Email):
                raise ValueError("Email Address is already registered.")

            cursor = self.connection.cursor()
            sql = 'SELECT * FROM Customers'
            cursor.execute(sql)
            x = list(cursor.fetchall())
            sql2 = 'INSERT INTO Customers(CustomerId, FirstName, LastName, Email, DateOfBirth, PhoneNumber, NumOrders, Address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
            para = (len(x)+1, FirstName, LastName, Email, DateOfBirth, Phone, NumOrders, Address)
            cursor.execute(sql2, para)
            self.connection.commit()
            self.connection.close()
            print("Customer registration successful.")
        except Exception as e:
            print(f"Error registering customer: {e}")

    def validate_customer_data(self, Email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, Email):
            raise ValueError("Invalid Email Address.")

    def is_Email_duplicate(self, Email):
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM Customers WHERE Email = %s'
        para = (Email,)
        cursor.execute(sql, para)
        x = len(list(cursor.fetchall()))
        if (x > 0):
            return True
        return False

    def get_customer_by_id(self, customer_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''SELECT * FROM Customers WHERE customer_id = %s'''
            para = (customer_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise CustomerNotFoundException('Invalid Customer ID')
            else:
                return Customers(*x)
        except CustomerNotFoundException as cnfe:
            print('An error occurred ',cnfe)
        except Exception as e:
            print('An error occurred ',e)
