class Shopping:
    catalogue = dict()
    cart = dict()
    def __init__(self, name, price, quantity):
        self.name= name
        self.price= price
        self.quantity= quantity
    def getItems(catalogue):    
        while True:
            id= int(input("Enter the item ID (0 to stop adding): "))
            if id == 0:
                break
            if id in catalogue.keys():
                c= input("Item with the same ID already exists. Replace? (yes/no): ")
                if c.lower() == "no":
                    continue
            name = input("Enter the item name: ")
            price = int(input("Enter the price: "))
            quant = int(input("Enter the quantity: "))
            catalogue[id]=Shopping(id, name, price, quant)
    def showItems(catalogue):
        print("ID:\tName:\tPrice:\tQuantity available:")
        for i in catalogue.items():
            print(f"{i.id}\t{i.name}\t{i.price}\t{i.quantity}")
    def showCart(cart):
        totalcost= 0
        print("ID:\tName:\tQuantity:\tTotal price:")
        for i in cart.items():
            print(f"{i.id}\t{i.name}\t{i.quantity}\t{i.price}")
            totalcost+= i.price
        print("Total amount= ",totalcost)
    while True:
        print("1) Update item list\n2) Buy items")
        ch= int(input("Enter your choice: "))
        if ch==1:
            catalogue= getItems(catalogue)
            print(catalogue)
        elif ch==2:
            print(catalogue)
            showItems(catalogue)
            while True:
                id= int(input("Enter the item ID (or 0 to stop): "))
                if(id==0):
                    break
                if id not in catalogue.keys():
                    print("No such item.")
                    continue
                print("Selected item: {}".format(catalogue[id].name))
                quant= int(input("Enter the number of {}: ".format(catalogue[id].name)))
                if(quant>catalogue[id].quantity):
                    print("There are only {} {}. Nothing added.".format(catalogue[id].quantity,catalogue[id].name))
                    continue
                catalogue[id].quantity-= quant
                cart[id] = list((catalogue[id].name,quant,quant*catalogue[id].price))
                print("{} {} added to cart.".format(quant, catalogue[id].name))
                
            print("Current cart: ")
            print(cart)
            showCart(cart)
            print("1) Checkout\n2) Change items")
            ch= int(input("Enter your choice: "))
            if ch==1:
                print("Thank you for shopping.")
                break
    