lookup= {"good":"great", "nice":"awesome"}
keylist= list(lookup.keys())
inp = input("Enter the string: ")
words = inp.split()
for i in keylist:
    inp=inp.replace(i, lookup[i])
print(inp)