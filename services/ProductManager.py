from custom_exception.CustomException import ProductNotFoundException
from models.Products import Products
from DBConnector.DBConnectivity import getDBConn

def getAllProducts() -> list:
    mydb = getDBConn()
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM Products')
    t = list(mycursor.fetchall())
    x = [Products(*list(i)) for i in t]
    return x

class ProductManager:
    def __init__(self):
        self.connection = getDBConn()

    def add_product(self, product: Products):
        try:
            if self.product_exists(product.get_product_id()):
                raise ValueError("Product with the same ProductID already exists.")

            cursor = self.connection.cursor()
            sql = '''INSERT INTO Products(ProductID, ProductName, Description, Price) VALUES(%s, %s, %s, %s)'''
            para = (product.get_product_id(), product.get_product_name(), product.get_description(), product.get_price())
            cursor.execute(sql, para)
            self.connection.commit()
            print(f"Product {product.get_product_id()} added successfully.")
        except Exception as e:
            print(f"Error adding product: {e}")

    def update_product(self, product: Products, new_price, new_description):
        try:
            # Check if the product with the given ProductID exists
            if not self.product_exists(product.get_product_id()):
                raise ValueError("Product with the given ProductID does not exist.")

            product.update_product_info(price = new_price, description = new_description)
            print(f"Product {product.get_product_id()} updated successfully.")
        except Exception as e:
            print(f"Error updating product: {e}")

    def remove_product(self, product_id):
        try:
            if not self.product_exists(product_id):
                raise ValueError("Product with the given ProductID does not exist.")

            if self.product_has_orders(product_id):
                raise ValueError("Product cannot be removed as it is associated with existing orders.")

            cursor = self.connection.cursor()
            sql = 'DELETE FROM Products WHERE ProductID = %s'
            para = (product_id,)
            cursor.execute(sql, para)
            self.connection.commit()
            print(f"Product {product_id} removed successfully.")
        except Exception as e:
            print(f"Error removing product: {e}")

    def product_exists(self, product_id):
        cursor = self.connection.cursor()
        sql = '''SELECT COUNT(*) FROM Products WHERE ProductID = %s'''
        para = (product_id,)
        cursor.execute(sql, para)
        x = len(list(cursor.fetchall()))
        return x > 0

    def product_has_orders(self, product_id):
        cursor = self.connection.cursor()
        sql = '''SELECT COUNT(OrderDetails.OrderID) AS Order_Number FROM Products
                JOIN OrderDetails
                ON Products.ProductID = OrderDetails.ProductID
                WHERE products.ProductID = %s GROUP BY products.ProductID'''
        para = (product_id, )
        cursor.execute(sql, para)
        x = len(list(cursor.fetchall()))
        return x > 0

    def list_all_products(self) -> list[Products]:
        return getAllProducts()

    def search_product(self, search_keyword):
        mycursor = self.connection.cursor()
        sql = '''SELECT * FROM Products WHERE UPPER(ProductName) LIKE UPPER(%s) OR UPPER(Description) LIKE UPPER(%s)'''
        para = ('%'+search_keyword+'%', '%'+search_keyword+'%')
        mycursor.execute(sql, para)
        t = list(mycursor.fetchall())
        x = [list(i) for i in t]
        return x

    def get_product_by_id(self, product_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * Products WHERE ProductID = %s
            '''
            para = (product_id,)
            my_cursor.execute(sql, para)
            x = my_cursor.fetchone()
            if x is None:
                raise ProductNotFoundException('Invalid product ID')
            else:
                return Products(*x)
        except ProductNotFoundException as pnfe:
            print('An error occurred: ', pnfe)
        except Exception as e:
            print('An error occurred: ', e)