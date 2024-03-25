inp = input("Enter the string: ")
l= inp.split(sep=" ")
unique = set(l)
d= {len(x):x for x in unique if inp.count(x)==1}
keys= list(d.keys())
keys.sort()
print(keys)
sortedwords= {d[k]:len(d[k]) for k in keys}
print(sortedwords)