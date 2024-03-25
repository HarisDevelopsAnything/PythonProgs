inp = input("Enter the string: ")
if len(inp)<3:
    print(inp)
else:
    out = inp+"ly" if inp.endswith("ing") else inp+"ing"
    print(out)