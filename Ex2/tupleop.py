l=tuple()
while True:
    print("1) Create tuple\n2) Check membership\n3) Create frequency table\n4) Delete tuple\n5) Show unique elements\n6) Find item occurences\n7) Find index\n8) Max value\n9) Min value\n10) Show tuple\n11) Quit")
    ch= int(input("Enter your choice: "))
    if(ch==1):
        l=eval(input("Enter the tuple: "))
        print(l)
    elif(ch==2):
        inp= int(input("What to check if present?: "))
        print("It is present." if inp in l else "It is not present.")
    elif(ch==3):
        elem= list(range(min(l), max(l)+1))
        for i in elem:
            if l.count(i)>0:
                print(i,"="*l.count(i), end="[{0}]\n".format(l.count(i)))
    elif(ch==4):
        inp= input("Are you sure you want to delete?(y/N): ")
        if(inp.upper()=='Y'):
            del(l)
        else:
            print("Delete cancelled by user.")
    elif(ch==5):
        ul=[]
        for i in l:
            if(i not in ul):
                ul.append(i)
        print("Unique elements= ",ul)
    elif(ch==6):
        inp= int(input("Item to find occurence?: "))
        print("Count of {0}= {1}".format(inp,l.count(inp)))
    elif(ch==7):
        inp= eval(input("Enter the element to find index: "))
        print("Element found at index: {0}".format(l.index(inp)))
    elif(ch==8):
        print(max(l))
    elif(ch==9):
        print(min(l))
    elif(ch==10):
        print("Current tuple: ",l)
    elif(ch==11):
        print("Quitting.")
        break
    