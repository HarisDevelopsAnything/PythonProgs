a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
s1=0
s2=0
for i in range(1,a):
    if a%i==0:
        s1+=i
for i in range(1,b):
    if b%i==0:
        s2+=i
if (s2/a) == (s1/b):
    print("Amicable numbers")
else:
    print("Not amicable numbers")