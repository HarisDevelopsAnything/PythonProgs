import billingOps as bops
catalogue = dict()
cart = dict()
while True:
    print("1) Update item list\n2) Buy items")
    ch= int(input("Enter your choice: "))
    if ch==1:
        catalogue= bops.getItems(catalogue)
        print(catalogue)
    elif ch==2:
        print(catalogue)
        bops.showItems(catalogue)
        while True:
            id= int(input("Enter the item ID (or 0 to stop): "))
            if(id==0):
                break
            if id not in catalogue.keys():
                print("No such item.")
                continue
            print("Selected item: {}".format(catalogue[id][0]))
            quant= int(input("Enter the number of {}: ".format(catalogue[id][0])))
            if(quant>catalogue[id][2]):
                print("There are only {} {}. Nothing added.".format(catalogue[id][2],catalogue[id][0]))
                continue
            catalogue[id][2]-= quant
            cart[id] = list((catalogue[id][0],quant,quant*catalogue[id][1]))
            print("{} {} added to cart.".format(quant, catalogue[id][0]))
            
        print("Current cart: ")
        print(cart)
        bops.showCart(cart)
        print("1) Checkout\n2) Change items")
        ch= int(input("Enter your choice: "))
        if ch==1:
            print("Thank you for shopping.")
            break



