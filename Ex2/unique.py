l=eval(input("Enter a list: "))
ul=[]
p=1
for i in l:
    if(i not in ul):
        ul.append(i)
        p*=i
print("Product of unique elements ",ul,"= ",p)