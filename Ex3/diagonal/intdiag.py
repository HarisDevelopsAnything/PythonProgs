import matrixOps as mops
size= int(input("Enter the size of square matrix: "))
l= list()
print("Enter the elements: ")
for i in range(0,size):
    l.append(list())
    for j in range(0,size):
        l[i].append(int(input("[{}][{}]: ".format(i,j))))
print("The matrix: ")
mops.showMatrix(l)
swap= mops.swapDiag(l)
print("After swap: ")
mops.showMatrix(swap)