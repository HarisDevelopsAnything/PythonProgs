inp= input("Enter the number: ")
l= len(inp)
n=int(inp)
temp= n
s=0
while n!=0:
    d= n%10
    s+= d**l
    n//=10
if temp==s:
    print("Armstrong")
else:
    print("Not armstrong")
