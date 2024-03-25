def getItems(catalogue):    
    while True:
        id= int(input("Enter the item ID (0 to stop adding): "))
        if id == 0:
            break
        if id in catalogue.keys():
            c= input("Item with the same ID already exists. Replace? (yes/no): ")
            if c.lower() == "no":
                continue
        catalogue[id] = list()
        name = input("Enter the item name: ")
        price = int(input("Enter the price: "))
        quant = int(input("Enter the quantity: "))
        catalogue[id].extend(list((name, price, quant)))
    return catalogue
def showItems(catalogue):
    print("ID:\tName:\tPrice:\tQuantity available:")
    for i,j in catalogue.items():
        print(f"{i}\t{j[0]}\t{j[1]}\t{j[2]}")
def showCart(cart):
    totalcost= 0
    print("ID:\tName:\tQuantity:\tTotal price:")
    for i,j in cart.items():
        print(f"{i}\t{j[0]}\t{j[1]}\t{j[2]}")
        totalcost+= j[2]
    print("Total amount= ",totalcost)


