from DBConnector.DBConnectivity import getDBConn


class Customers:
    def __init__(self, CustomerId, FirstName, LastName, Email, DateOfBirth, PhoneNumber):
        self.connection = getDBConn()
        self.CustomerId = CustomerId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.DateOfBirth = DateOfBirth
        self.PhoneNumber = PhoneNumber

def CalculateTotalOrders(self):
    cursor = self.connection.cursor()
    sql = 'SELECT %s,COUNT(*) AS TotalOrders from Orders where CustomerId = %s;'
    params =(self.CustomerId , self.CustomerId)
    cursor.execute(sql, params)
    temp = list(cursor.fetchone())
    return temp[1]

def getCustomerDetails(self):
    details = f"CustomerId : {self.CustomerId}"
    details += f"Name: {self.FirstName} {self.LastName}"
    details += f"Email: {self.Email}"
    details += f"DateOfBirth: {self.DateOfBirth}"
    details += f"PhoneNumber: {self.PhoneNumber}"
    return details

def UpdateCustomerInfo(self,Email,Address,PhoneNumber):
    if Email:
        cursor = self.connect.cursor()
        sql = 'UPDATE Customers SET Email = %s WHERE CustomerId = %s'
        params = (Email, self.CustomerId)
        cursor.execute(sql, params)
        self.Email = Email

    if PhoneNumber:
        cursor = self.connection.cursor()
        sql = 'UPDATE Customers SET PhoneNumber = %s WHERE CustomerId = %s'
        params = (PhoneNumber,self.CustomerId)
        cursor.execute(sql, params)
        self.PhoneNumber = PhoneNumber

    if Address:
        cursor = self.connect.cursor()
        sql = 'UPDATE Customers SET Address = %s WHERE CustomersId = %s'
        params = (Address, self.CustomerId)
        cursor.execute(sql, params)
        self.Address = Address

    def get_num_orders(self):
        return self.NoOfOrders

    # Getter for customer_id
    def get_customer_id(self):
        return self.CustomerId

    # Getter for first_name
    def get_first_name(self):
        return self.FirstName

    # Getter for last_name
    def get_last_name(self):
        return self.LastName

    # Getter for email
    def get_email(self):
        return self.Emailb

    # Getter for phone
    def get_phone(self):
        return self.PhoneNumber

    # Getter for address
    def get_address(self):
        return self.Address

    def get_dob(self):
        return self.DateOfBirth




