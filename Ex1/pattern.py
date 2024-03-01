l= int(input("Enter the height: "))
n=1
for i in range(l):
    for j in range(l):
        if(j>=(l-i-1)):
            print(n,end='')
            n+=1
        else:
            print(end=' ')
    print()