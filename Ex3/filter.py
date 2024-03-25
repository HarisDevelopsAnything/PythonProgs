inp= input("Enter the string: ")
sub= input("Enter the substring to search: ")
l= inp.split(sep=" ")
issub= lambda x: sub in x
res= list(filter(issub, l))
print("List of words containing the substring: ",res)