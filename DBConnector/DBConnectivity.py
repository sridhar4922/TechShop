import pyodbc


class getDBConn:


    @staticmethod
    def getDBConn():
        server = r'LAPTOP-J4AMUSBP\SQLEXPRESS'
        database = 'TechShop'

        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        try:
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            print(f"Error connecting: {str(e)}")


# Example usage:
conn = getDBConn.getDBConn()
if conn:
    print("Connection established successfully.")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Use the connection object for further operations
else:
    print("Failed to establish connection.")
