from models.Orders import Orders
from models.Products import Products
from services.CustomerManager import CustomerManager
from services.ProductManager import ProductManager
from services.OrderManager import OrderManager
from services.InventoryManager import InventoryManager

def main_menu():
    print("Welcome to TechShop!")
    print("1. Customer Management")
    print("2. Product Management")
    print("3. Oders Management")
    print("4. Inventory Management")
    print("5. Exit")

def customer_management_menu():
    print("\nCustomer Management Menu:")
    print("1. Register Customer")
    print("2. View Customer Details")
    print("3. Update Customer Information")
    print("4. Back to Main Menu")

def product_management_menu():
    print("\nProduct Management Menu:")
    print("1. Add Product")
    print("2. View Product Details")
    print("3. Update Product Information")
    print("4. Back to Main Menu")

def Oders_management_menu():
    print("\nOders Management Menu:")
    print("1. Place Oders")
    print("2. View Oders Details")
    print("3. Update Oders Status")
    print("4. Cancel Oders")
    print("5. Back to Main Menu")

def inventory_management_menu():
    print("\nInventory Management Menu:")
    print("1. Add to Inventory")
    print("2. Remove from Inventory")
    print("3. View Inventory Details")
    print("4. List Low Stock Products")
    print("5. List Out of Stock Products")
    print("6. List All Products in Inventory")
    print("7. Back to Main Menu")

if __name__ == "__main__":
    CustomerManager = CustomerManager()
    product_manager = ProductManager()
    order_manager = OrderManager()
    inventory_manager = InventoryManager()

    while True:
        main_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            while True:
                customer_management_menu()
                customer_choice = input("Enter your choice (1-4): ")

                if customer_choice == "1":
                    CustomerManager.register_customer(
                        input("Enter First Name: "),
                        input("Enter Last Name: "),
                        input("Enter Email: "),
                        input("Enter DOB: "),
                        input("Enter Phone: "),
                        0,
                        input("Enter Address: ")
                    )
                elif customer_choice == "2":
                    temp_customer = CustomerManager.get_customer_by_id(customer_id=input('Enter CustomerID: '))
                    print(temp_customer.get_customer_details())
                elif customer_choice == "3":
                    temp_customer = CustomerManager.get_customer_by_id(customer_id=input('Enter CustomerID: '))
                    temp_customer.update_customer_info(email=input('Enter new email'),
                                                       phone=input('Enter new phone'),
                                                       address=input('Enter new address'))

                elif customer_choice == "4":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == "2":
            while True:
                product_management_menu()
                product_choice = input("Enter your choice (1-4): ")

                if product_choice == "1":
                    product_manager.add_product(
                        Products(input("Enter Product ID: "),
                        input("Enter Product Name: "),
                        input("Enter Description: "),
                        float(input("Enter Price: ")))
                    )
                elif product_choice == "2":
                    temp_product = ProductManager.get_product_by_id(input('Enter Product ID'))
                    print(temp_product.get_product_details())
                elif product_choice == "3":
                    temp_product = product_manager.get_product_by_id(input('Enter Product ID'))
                    temp_product.update_product_info(price=input('Enter New Product Price'), description=input('Enter New Product Description'))
                elif product_choice == "4":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == "3":
            while True:
                order_manager()
                order_choice = input("Enter your choice (1-5): ")
                cm = CustomerManager()

                if order_choice == "1":
                    order_manager.add_order(Orders(
                        input('Enter Order ID: '),
                        cm.get_customer_by_id(input('Enter Customer ID: ')),
                        input('Enter Order Date: '),
                        input('Enter Total Amount: '),
                        input('Enter Order Status: ')
                    ))
                elif order_choice == "2":
                    temp_Data = order_manager.get_order_by_id(input(
                        'Enter Order ID: '
                    ))
                    print(temp_Data.get_order_details())
                elif order_choice == "3":
                    temp_Data = order_manager.get_order_by_id(input(
                        'Enter Order ID: '
                    ))
                    temp_Data.update_order_status(input('Enter New Status'))
                elif order_choice == "4":
                    temp_Data = order_manager.get_order_by_id(input(
                        'Enter Order ID: '
                    ))
                    temp_Data.cancel_order()
                elif order_choice == "5":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        elif choice == "4":
            while True:
                inventory_management_menu()
                inventory_choice = input("Enter your choice (1-7): ")

                if inventory_choice == "1":
                    inventory_manager.add_to_inventory(input('Enter Product ID: '), input('Enter Product Quantity: '))
                elif inventory_choice == "2":
                    inventory_manager.remove_from_inventory(input('Enter Product ID: '), input('Enter Product Quantity: '))
                elif inventory_choice == "3":
                    inventory_manager.list_all_products()
                elif inventory_choice == "4":
                    inventory_manager.list_low_stock_products(2)
                elif inventory_choice == "5":
                    inventory_manager.list_out_of_stock_products()
                elif inventory_choice == "6":
                    inventory_manager.list_all_products()
                elif inventory_choice == "7":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")

        elif choice == "5":
            print("Exiting TechShop. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")