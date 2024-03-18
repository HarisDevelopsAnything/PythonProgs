inp = input("Enter the string: ")
l= list(inp)
c= input("What character to replace?: ")[0]
r= input("What to replace it with?: ")[0]
f= lambda x: r if x==c else x
newstr= list(map(f,l))
print(''.join(newstr))