checklength = lambda x: len(x)>=8 and len(x)<=15
checkspecial = lambda x: not x.isalnum() and x!=' '
checklower = lambda x: x.islower()
checkupper = lambda x: x.isupper()
checkdigit = lambda x: x.isdigit()
checkspaces = lambda x: x==' '
while True:
    sp= 0
    lw= 0
    up= 0
    dg= 0
    space = 0
    valid= True
    pwd= input("Enter your password: ")
    if(not checklength(pwd)):
        print("Length should be 8 to 15 characters")
        valid= False
    for i in pwd:
        if(checkspecial(i)):
            sp+=1
        elif(checklower(i)):
            lw+=1
        elif(checkupper(i)):
            up+=1
        elif(checkdigit(i)):
            dg+=1
        elif(checkspaces(i)):
            space+=1
    if(sp==0):
        print("Password must contain special characters")
        valid= False
    if(lw==0):
        print("Password must contain atleast 1 lowercase")
        valid= False
    if(up==0):
        print("Password must contain atleast 1 uppercase")
        valid= False
    if(dg==0):
        print("Password must contain digits")
        valid= False
    if(space>0):
        print("Password must not contain spaces")
        valid= False
    if(valid):
        print("Password is valid.")
        break



    
