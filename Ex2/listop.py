l=list()
while True:
    print("1) Create list\n2) Insert new item\n3) Append item\n4) Delete matching item\n5) Delete item at index\n6) Find item occurences\n7) Extend list\n8) Max value\n9) Min value\n10) Show list\n11) Quit")
    ch= int(input("Enter your choice: "))
    if(ch==1):
        l=eval(input("Enter the list: "))
        print(l)
    elif(ch==2):
        inp= input("What to insert?: ")
        ind= int(input("Where to insert?: "))
        l.insert(ind, inp)
        print(l)
    elif(ch==3):
        inp= input("What to append?: ")
        l.append(inp)
    elif(ch==4):
        inp= input("What to delete?: ")
        l.remove(inp)
    elif(ch==5):
        inp= int(input("Which index to delete?: "))
        l.pop(inp)
    elif(ch==6):
        inp= int(input("Item to find occurence?: "))
        print("Count of {0}= {1}".format(inp,l.count(inp)))
    elif(ch==7):
        inp= eval(input("Enter the list to extend: "))
        l.extend(inp)
    elif(ch==8):
        print(max(l))
    elif(ch==9):
        print(min(l))
    elif(ch==10):
        print("Current list: ",l)
    elif(ch==11):
        print("Quitting.")
        break
    