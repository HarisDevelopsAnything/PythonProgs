inp = input("Enter the string: ")
l= list(inp)
lowerlist= []
for i in l:
    if ord(i)>=65 and ord(i)<=90:
        lowerlist.append(chr(ord(i)+32))
    else:
        lowerlist.append(i)
out = ''.join(lowerlist)
print(out)
