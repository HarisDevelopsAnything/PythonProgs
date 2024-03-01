import keyword, time

a= keyword.kwlist
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
       print(a[i][j], end='')
       time.sleep(0.3)
    print("\n")
