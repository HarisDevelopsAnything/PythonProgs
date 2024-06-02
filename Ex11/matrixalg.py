from mathrix import algebra, matrix
print("1) Algebraic operation 2) Matrix operation 3) Exit")
ch= int(input("Enter the choice: "))
if ch==1:
    a= int(input("Enter the first number: "))
    b= int(input("Enter the first number: "))
    print(f"Sum: {algebra.add(a,b)}")
    print(f"Diff: {algebra.sub(a,b)}")
    print(f"Product: {algebra.mul(a,b)}")
    print(f"Div: {algebra.div(a,b)}")
    print(f"Mod: {algebra.mod(a,b)}")
elif ch==2:
    m= int(input("Enter the rows of the matrix: "))
    n= int(input("Enter the cols of the matrix: "))
    m1= list()
    m2= list()
    print("Enter the matrix 1:")
    for i in range(m):
        row= list()
        for j in range(n):
            row.append(int(input(f"[{i}][{j}]: ")))
        m1.append(row)
    print("Enter the matrix 2:")
    for i in range(m):
        row= list()
        for j in range(n):
            row.append(int(input(f"[{i}][{j}]: ")))
        m2.append(row)
    sum= matrix.add(m1, m2)
    diff= matrix.sub(m1, m2)
    matrix.show(sum)
    