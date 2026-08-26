import hashlib
import json
import secrets
from pathlib import Path


USERS_FILE = Path(__file__).with_name("users.json")


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


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        current_quantity = self.items.get(product.item_id, 0)
        if current_quantity + quantity > product.quantity:
            print("Not enough stock for that cart quantity.")
            return

        self.items[product.item_id] = current_quantity + quantity
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def display(self, products):
        if not self.items:
            print("Your cart is empty.")
            return

        total = 0
        print("Shopping cart:")
        for item_id, quantity in self.items.items():
            product = products[item_id]
            subtotal = product.price * quantity
            total += subtotal
            print(f"{product.name} x {quantity} = P{subtotal:.2f}")
        print(f"Total: P{total:.2f}")

    def remove(self, product_id, quantity):
        if product_id not in self.items:
            print("That product is not in your cart.")
        elif quantity <= 0:
            print("Quantity must be greater than 0.")
        elif quantity >= self.items[product_id]:
            del self.items[product_id]
            print("Product removed from cart.")
        else:
            self.items[product_id] -= quantity
            print("Cart quantity updated.")

    def checkout(self, products):
        if not self.items:
            print("Your cart is empty.")
            return

        if any(products[item_id].quantity < quantity for item_id, quantity in self.items.items()):
            print("Checkout failed because some items no longer have enough stock.")
            return

        total = sum(products[item_id].price * quantity for item_id, quantity in self.items.items())
        for item_id, quantity in self.items.items():
            products[item_id].quantity -= quantity
        self.items.clear()
        print(f"Checkout complete. Total paid: P{total:.2f}")


def load_users():
    if not USERS_FILE.exists():
        return {}
    try:
        with USERS_FILE.open("r", encoding="utf-8") as users_file:
            return json.load(users_file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the user database.")
        return {}


def save_users(users):
    with USERS_FILE.open("w", encoding="utf-8") as users_file:
        json.dump(users, users_file, indent=2)


def hash_password(password, salt=None):
    salt = salt or secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), 200_000
    ).hex()
    return salt, password_hash


def register(users):
    username = input("Choose a username: ").strip()
    if not username or username in users:
        print("That username is unavailable.")
        return
    password = input("Choose a password: ")
    if not password:
        print("Password cannot be empty.")
        return
    salt, password_hash = hash_password(password)
    users[username] = {"salt": salt, "password_hash": password_hash}
    save_users(users)
    print("Account created. You can now log in.")


def login(users):
    username = input("Username: ").strip()
    account = users.get(username)
    if account is None:
        print("Invalid username or password.")
        return None
    salt, password_hash = hash_password(input("Password: "), account["salt"])
    if not secrets.compare_digest(password_hash, account["password_hash"]):
        print("Invalid username or password.")
        return None
    print(f"Welcome, {username}!")
    return username


def authenticate(users):
    while True:
        print("\n1. Log in")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            username = login(users)
            if username is not None:
                return username
        elif choice == "2":
            register(users)
        elif choice == "3":
            return None
        else:
            print("Please choose 1, 2, or 3.")


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
    try:
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("Price and quantity must be valid numbers.")
        return next_item_id
    if product_price < 0 or product_quantity < 0:
        print("Price and quantity cannot be negative.")
        return next_item_id
    products[next_item_id] = Product(
        next_item_id, product_name, product_price, product_quantity
    )
    print("Product added successfully!")
    products[next_item_id].display_info()
    return next_item_id + 1


def main():
    products = {}
    next_item_id = 1
    users = load_users()

    print("-- SARI SARI STORE MANAGEMENT PROGRAM --")
    print("Developed by: Mc")

    while True:
        username = authenticate(users)
        if username is None:
            print("Thank you for using the Sari Sari Store Management Program.")
            break
        cart = ShoppingCart()

        while True:
            print("\n" + "--" * 30)
            print("1. Add a new product")
            print("2. Sell items")
            print("3. Restock items")
            print("4. Remove items")
            print("5. View available products")
            print("6. Add item to shopping cart")
            print("7. View shopping cart")
            print("8. Remove item from cart")
            print("9. Checkout")
            print("10. Log out")

            try:
                choice = int(input("Enter your choice (1-10): "))
            except ValueError:
                print("Please enter a number from 1 to 10.")
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
                product = select_product(products)
                if product is not None:
                    try:
                        cart.add(product, int(input("Enter quantity to add: ")))
                    except ValueError:
                        print("Quantity must be a whole number.")
            elif choice == 7:
                cart.display(products)
            elif choice == 8:
                cart.display(products)
                try:
                    cart.remove(int(input("Enter product ID to remove: ")), int(input("Enter quantity to remove: ")))
                except ValueError:
                    print("Product ID and quantity must be whole numbers.")
            elif choice == 9:
                cart.checkout(products)
            elif choice == 10:
                print(f"Goodbye, {username}. You have been logged out.")
                break
            else:
                print("Please choose an option from 1 to 10.")


if __name__ == "__main__":
    main()
