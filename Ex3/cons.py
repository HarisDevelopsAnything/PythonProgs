inp = input("Enter the string: ")
l= list(inp)
vow= {'a','e','i','o','u'}
c=0
for i in inp:
    if i.lower() not in vow and i.isnumeric()==False and i!=' ':
        c+=1
print("Number of consonants= ",c)
isvowel = lambda x: x.lower() in vow
vowels = list(filter(isvowel, l))
print("Vowels in the string: ",vowels)