s1= set()
s2= set()
while True:
    print("1) Create sets\n2) Update set 1\n3) Update set 2\n4) Delete from set 1\n5) Delete from set 2\n6) Union\n7) Intersection\n8) Symmetric difference\n9) Check subset\n10) Check superset\n11) Quit")
    ch= int(input("Enter your choice: "))
    if(ch==1):
        l=eval(input("Enter the set 1: "))
        s1= set(l)
        l=eval(input("Enter the set 2: "))
        s2= set(l)
    elif(ch==2):
        inp= input("What to insert?: ")
        s1.update(inp)
        print(l)
    elif(ch==3):
        inp= input("What to insert?: ")
        s2.update(inp)
    elif(ch==4):
        inp= int(input("What to delete?: "))
        s1.discard(inp)
    elif(ch==5):
        inp= int(input("What to delete?: "))
        s2.discard(inp)
    elif(ch==6):
        print("Union: ",s1.union(s2))
    elif(ch==7):
        print("Intersection: ",s1.intersection(s2))
    elif(ch==8):
        print("Symmetric difference: ", s1.difference(s2))
    elif(ch==9):
        print("s1 is a subset of s2" if s1.issubset(s2) else "s1 is not a subset of s2")
    elif(ch==10):
        print("s1 is a superset of s2" if s1.issuperset(s2) else "s1 is not a superset of s2")
    elif(ch==11):
        print("Quitting.")
        break
    