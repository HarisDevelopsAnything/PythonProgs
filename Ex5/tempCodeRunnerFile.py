import random
class Shopping:
    catalogue = {}
    cart = {}
    billingID= ""
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    @staticmethod
    def greeter(user):
        print("="*20)
        print("Hey {}, Welcome to Mepco Shopping!".format(user))
        Shopping.billingID= str(random.randint(10**9, (10**10)-1))
        print("Your billing ID: ",Shopping.billingID)
        print("="*20)

    @classmethod
    def get_items(cls):
        while True:
            item_id = int(input("Enter the item ID (0 to stop adding): "))
            if item_id == 0:
                break
            if item_id in cls.catalogue:
                choice = input("Item with the same ID already exists. Replace? (yes/no): ")
                if choice.lower() == "no":
                    continue
            name = input("Enter the item name: ")
            price = float(input("Enter the price: "))
            quantity = int(input("Enter the quantity: "))
            cls.catalogue[item_id] = Shopping(item_id, name, price, quantity)

    @classmethod
    def show_items(cls):
        print("ID:\tName:\tPrice:\tQuantity available:")
        for item in cls.catalogue.values():
            print(f"{item.id}\t{item.name}\t{item.price}\t{item.quantity}")

    @classmethod
    def show_cart(cls):
        total_cost = 0
        print("ID:\tName:\tQuantity:\tTotal price:")
        for item_id, details in cls.cart.items():
            name, quantity, price = details
            print(f"{item_id}\t{name}\t{quantity}\t{price}")
            total_cost += price
        print("Total amount =", total_cost)

    @classmethod
    def buy_items(cls):
        cls.show_items()
        while True:
            item_id = int(input("Enter the item ID (or 0 to stop): "))
            if item_id == 0:
                break
            if item_id not in cls.catalogue:
                print("No such item.")
                continue
            print("Selected item:", cls.catalogue[item_id].name)
            quantity = int(input(f"Enter the number of {cls.catalogue[item_id].name}: "))
            if quantity > cls.catalogue[item_id].quantity:
                print(f"There are only {cls.catalogue[item_id].quantity} {cls.catalogue[item_id].name}. Nothing added.")
                continue
            cls.catalogue[item_id].quantity -= quantity
            cls.cart[item_id] = [cls.catalogue[item_id].name, quantity, quantity * cls.catalogue[item_id].price]
            print(f"{quantity} {cls.catalogue[item_id].name} added to cart.")
        print("Current cart: ")
        cls.show_cart()
        print("Billing ID: ",billingID)
        while True:
            choice = int(input("1) Checkout\n2) Change items\nEnter your choice: "))
            if choice == 1:
                print("Thank you for shopping.")
                return
            elif choice == 2:
                cls.buy_items()
user= input("Enter your name: ")
Shopping.greeter(user)
while True:
    print("1) Update item list\n2) Buy items\n3) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Shopping.get_items()
    elif choice == 2:
        Shopping.buy_items()
    elif choice == 3:
        break
