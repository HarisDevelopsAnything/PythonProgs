t= ((1,2,3),(4,5,6),(7,8,9))
rowsum=[0 for i in range(0,3)]
colsum=[0 for i in range(0,3)]
for i in range(len(t)):
    for j in range(len(t[i])):
        rowsum[i]+= t[i][j]
        colsum[j]+= t[i][j]
print(rowsum,colsum)