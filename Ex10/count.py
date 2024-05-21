name= input("Enter the file name: ")
try:
    f= open(name, "r")
    words= len(f.read().split(sep=" "))
    f.seek(0)
    lines= len(f.readlines())
    f.seek(0)
    ch= input("Enter the character to search: ")[0]
    occ= f.read().count(ch)
    print(f"No. of words: {words}")
    print(f"No. of lines: {lines}")
    print(f"Occurences of {ch}: {occ}")
except Exception as e:
    print("Error in opening file!")
finally:
    f.close()