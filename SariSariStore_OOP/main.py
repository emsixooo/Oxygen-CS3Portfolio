class Product:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"ID: {self.item_id} | {self.name} | Price: ₱{self.price:.2f} | Quantity: {self.quantity}")

    def sell(self, quantity):
        if 0 < quantity <= self.quantity:
            self.quantity -= quantity
            print(f"{quantity} {self.name}(s) sold.")
        elif quantity <= 0:
            print("Quantity must be greater than 0.")
        else:
            print("Not enough stock.")

    def restock(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            self.quantity += amount
            print(f"Restocked {amount} item(s). New quantity: {self.quantity}")

    def remove(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount <= self.quantity:
            self.quantity -= amount
            print(f"Removed {amount} item(s). New quantity: {self.quantity}")
        else:
            print("Not enough stock to remove that amount.")


def display_products(products):
    if not products:
        print("No products available.")
        return

    print("Available products:")
    for product in products.values():
        product.display_info()


def select_product(products):
    if not products:
        print("No products available.")
        return None

    display_products(products)
    try:
        item_id = int(input("Enter product ID: "))
    except ValueError:
        print("Please enter a valid product ID.")
        return None

    product = products.get(item_id)
    if product is None:
        print("Product ID not found.")
    return product


def add_product(products, next_item_id):
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    products[next_item_id] = Product(
        next_item_id, product_name, product_price, product_quantity
    )
    print("Product added successfully!")
    products[next_item_id].display_info()
    return next_item_id + 1


def main():
    products = {}
    next_item_id = 1

    print("-- SARI SARI STORE MANAGEMENT PROGRAM --")
    print("Developed by: Mc")

    while True:
        print("\n" + "--" * 30)
        print("1. Add a new product")
        print("2. Sell items")
        print("3. Restock items")
        print("4. Remove items")
        print("5. View available products")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            next_item_id = add_product(products, next_item_id)
        elif choice == 2:
            product = select_product(products)
            if product is not None:
                product.sell(int(input("Enter quantity to sell: ")))
        elif choice == 3:
            product = select_product(products)
            if product is not None:
                product.restock(int(input("Enter amount to restock: ")))
        elif choice == 4:
            product = select_product(products)
            if product is not None:
                product.remove(int(input("Enter amount to remove: ")))
        elif choice == 5:
            display_products(products)
        elif choice == 6:
            print("Thank you for using the Sari Sari Store Management Program.")
            break
        else:
            print("Please choose an option from 1 to 6.")


if __name__ == "__main__":
    main()
