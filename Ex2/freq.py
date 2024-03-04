l= eval(input("Enter the list: "))
f= int(input("Enter the frequency: "))
print("Elements having more than {0} occurences: ".format(f))
elem= list(range(min(l), max(l)+1))
for i in elem:
    if l.count(i)>f:
        print("{0} - {1} occurences".format(i, l.count(i)))