def add(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Incompatible matrices!")
        return
    sum= list()
    for i in range(len(a)):
        row= list()
        for j in range(len(a[0])):
            row.append(a[i][j]+ b[i][j])
        sum.append(row)
    return sum
def sub(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Incompatible matrices!")
        return
    sum= list()
    for i in range(len(a)):
        row= list()
        for j in range(len(a[0])):
            row.append(a[i][j]- b[i][j])
        sum.append(row)
    return sum
def show(a):
    for i in a:
        for j in i:
            print(j, end=' ')
        print()