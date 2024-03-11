d= eval(input("Enter a dictionary with lists: "))
print("Current dictionary: ",d)
k= list(d.keys())
k.sort()
d_sorted= {key:sorted(d[key]) for key in k}
print("Sorted dictionary (key sorted): ",d_sorted)