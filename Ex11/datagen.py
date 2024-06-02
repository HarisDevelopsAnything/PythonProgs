import csv
import random
file= open("fitness_data.csv", 'w')
csvfile= csv.writer(file)
for i in range(0,31):
    row= list()
    for j in range(0,5):
        row.append(random.randint(1500, 15000))
    csvfile.writerow(row)
file.close()