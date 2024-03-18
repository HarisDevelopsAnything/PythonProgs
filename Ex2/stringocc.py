l= eval(input("Enter the list of strings"))
s= set(l)
occ= [(l.count(x),x) for x in s]
print(occ)