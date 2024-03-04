inp= input("Enter the string: ")
letters= set(inp.upper())
f=0
for i in range(65,91):
    if chr(i) not in letters:
        f+=1
if(f>0):
    print("The string is not a pangram (misses {0} letters)".format(f))
else:
    print("The string is a pangram.")