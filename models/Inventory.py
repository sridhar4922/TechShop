
from models.Products import Products
from DBConnector.DBConnectivity import getDBConn
class Inventory:
    def __init__(self, InventoryId, Products: Products, QuantityInStock, LastStockUpdate):
        self.connection = getDBConn()
        self.InventoryId = InventoryId
        self.Products = Products
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    # Getter for inventory_id
    def get_inventory_id(self):
        return self.InventoryId

    # Getter for product
    def get_product(self):
        return self.Products

    # Setter for product
    def set_product(self, Products:Products):
        cursor = self.connection.cursor()
        sql = 'UPDATE Inventory SET ProductID = %s WHERE Inventory = %s'
        params = (Products.get_product_id(), self.InventoryId)
        cursor.execute(sql, params)
        self.Products = Products

    # Getter for quantity_in_stock
    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    # Setter for quantity_in_stock
    def set_quantity_in_stock(self, QuantityInStock):
        cursor = self.connection.cursor()
        sql = 'UPDATE Inventory SET QuantityInStock = %s WHERE InventoryId = %s'
        params = (QuantityInStock
                , self.InventoryId)
        cursor.execute(sql, params)
        self.QuantityInStock = self.QuantityInStock

    # Getter for last_stock_update
    def get_last_stock_update(self):
        return self.LastStockUpdate

    # Setter for last_stock_update
    def set_last_stock_update(self, LastStockUpdate):
        cursor = self.connection.cursor()
        sql = 'UPDATE Inventory SET LastStockUpdate = %s WHERE InventoryId = %s'
        para = (LastStockUpdate, self.InventoryId)
        cursor.execute(sql, para)
        self.__last_stock_update = LastStockUpdate

    def get_product(self):
        return self.Products

    def get_quantity_in_stock(self):
        return self.QuantityInStock

    def add_to_inventory(self, quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE Inventory SET QuantityInStock = %s WHERE InventoryId = %s'
        params = (self.__quantity_in_stock + quantity, self.InventoryId)
        cursor.execute(sql, params)
        self.QuantityInStock += quantity

    def remove_from_inventory(self, quantity):
        if self.__quantity_in_stock >= quantity:
            cursor = self.connection.cursor()
            sql = 'UPDATE inventory SET QuantityInStock = %s WHERE InventoryId = %s'
            params = (self.QuantityInStock - quantity, self.InventoryId)
            cursor.execute(sql, params)
            self.__quantity_in_stock -= quantity
        else:
            print("Error: Insufficient quantity in stock.")
            return

    def update_stock_quantity(self, new_quantity):
        cursor = self.connection.cursor()
        sql = 'UPDATE Inventory SET QuantityInStock = %s WHERE InventoryId = %s'
        para = (new_quantity, self.InventoryId)
        cursor.execute(sql, para)
        self.QuantityInStock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.QuantityInStock >= quantity_to_check

    def get_inventory_value(self):
        return self.QuantityInStock * self.Products.get_price()

    def list_low_stock_products(self, threshold):
        if self.QuantityInStock < threshold:
            return f"{self.Products.get_product_name()} is below the threshold with {self.QuantityInStock} units."

    def list_out_of_stock_products(self):
        if self.QuantityInStock == 0:
            return f"{self.Products.get_product_name()} is out of stock."
        else:
            return f"No product is out of stock"

    def list_all_products(self):
        return f"Product: {self.Products.get_product_details()}, Quantity in Stock: {self.QuantityInStock}"
