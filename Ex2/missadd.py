s1= set(eval(input("Enter the first set: ")))
s2= set(eval(input("Enter the second set: ")))
print("Missing elements from s1: ", s2.difference(s1))
print("Additional elements in s1: ", s1.difference(s2))
