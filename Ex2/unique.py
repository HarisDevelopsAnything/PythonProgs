l=eval(input("Enter a list: "))
ul=[]
for i in l:
    if(i not in ul):
        ul.append(i)
print(ul)