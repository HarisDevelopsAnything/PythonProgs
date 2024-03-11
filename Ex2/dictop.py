l=list()
while True:
    print("1) Create dictionary\n2) Insert new item\n3) Clear dictionary\n4) Delete item\n5) Access data using key\n6) Delete last item\n7) Show dictionary\n8) Quit")
    ch= int(input("Enter your choice: "))
    if(ch==1):
        l=eval(input("Enter the dictionary: "))
        print(l)
    elif(ch==2):
        inp= input("What to insert?: ")
        ind= input("Key?: ")
        l[ind]=inp
        print(l)
    elif(ch==3):
        l.clear()
        print("Dictionary cleared.")
    elif(ch==4):
        inp= input("What to delete(key)?: ")
        del l[inp]
    elif(ch==5):
        inp= input("Enter the key: ")
        print(l[inp])
    elif(ch==6):
        print("Deleted ",l.popitem())
    elif(ch==7):
        print("Current dictionary: ",l)
    elif(ch==8):
        print("Quitting.")
        break
    