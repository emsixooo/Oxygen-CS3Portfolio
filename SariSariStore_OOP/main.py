class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Function to display product information
    def display_info(self):
        print("Product:", self.name)
        print("Price: ₱", self.price)
        print("Quantity:", self.quantity)

    #Function to display product information
    def display_info(self):
        print("Product:", self.name)
        print("Price: ₱", self.price)
        print("Quantity:", self.quantity)

    #Function to sell items from the product's quantity
    def sell(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print(quantity, self.name, "sold.")
        else:
            print("Not enough stock.")

    #Function to add items to the product's quantity
    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(f"Restocked {amount} item(s).")
            print(f"New quantity: {self.quantity}")

    #Function to remove items from the product's quantity
    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} item(s).")
            print(f"New quantity: {self.quantity}")
        else:
            print("Not enough stock to remove that amount.")
            
# Main interface for the Sari Sari Store Management Program
print("-- SARI SARI STORE MANAGEMENT PROGRAM --")
print("Developed by: Mc")
print("--" * 30)
print("Do you wish to:")
print("1. Add a new product")
print("2. Sell items")
print("3. Restock items")
print("4. Remove items")

choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = Product(product_name, product_price, product_quantity)
    print("--" * 30)
    print("Product added successfully!")
    product.display_info()
elif choice == 2:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = Product(product_name, product_price, product_quantity)
    sell_quantity = int(input("Enter quantity to sell: "))
    print("--" * 30)    
    product.sell(sell_quantity)
elif choice == 3:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = Product(product_name, product_price, product_quantity)
    restock_amount = int(input("Enter amount to restock: "))
    product.restock(restock_amount)
elif choice == 4:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = Product(product_name, product_price, product_quantity)
    remove_amount = int(input("Enter amount to remove: "))
    product.remove(remove_amount)
elif choice == 5:
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = Product(product_name,product_price, product_quantity)
    remove_amount = int(input("Enter amount to remove: "))
    product.remove(remove_amount)
