def showMatrix(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat)):
            print(mat[i][j],end=" ")
        print()
def swapDiag(mat):
    for i in range(0,len(mat)):
        for j in range(0, len(mat)):
            if i==j:
                t= mat[i][j]
                mat[i][j]= mat[i][len(mat)-j-1]
                mat[i][len(mat)-j-1]= t
    return mat