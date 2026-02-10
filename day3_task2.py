#Task 3 : Multilevel Inheritance Program – Online Shopping System
#Problem Statement
#Create a program for an Online Shopping System using Multilevel Inheritance.
#Requirements
#Parent Class: Product
#Attributes:
#product_name
#price
#Method:
#display_product()
#Child Class: ElectronicProduct (inherits from Product)
#Attributes:
#brand
#warranty
#Method:
#display_electronic_product()
#Grandchild Class: MobilePhone (inherits from ElectronicProduct)
#Attributes:
#ram
#storage
#Method:
#display_mobile_details()
#Create one object of MobilePhone and display all details.




# Parent Class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


# Child Class
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


# Grandchild Class
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


# Create object
mobile = MobilePhone("iPhone 15", 80000, "Apple", "1 Year", "8GB", "256GB")

# Display all details
mobile.display_product()
mobile.display_electronic_product()
mobile.display_mobile_details()