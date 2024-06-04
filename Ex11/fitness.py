import numpy as np
import matplotlib.pyplot as plt
import math
with open('fitness_data.csv', 'r') as f:
    names= list(f.readline()[0:-1].split(sep=","))
data = np.loadtxt('fitness_data.csv', delimiter=',', skiprows=1)
mean_counts = np.mean(data, axis=0)
median_counts = np.median(data, axis=0)
std_dev_counts = np.std(data, axis=0)
max_counts = np.max(data, axis=0)
min_counts = np.min(data, axis=0)
below_5000 = np.sum(data < 5000, axis=0)
above_or_equal_10000 = np.sum(data >= 10000, axis=0)
for i in range(data.shape[1]):
    print(f"{names[i]}:")
    print(f"Mean: {math.ceil(mean_counts[i])}, Median: {math.ceil(median_counts[i])}, Std Dev: {math.ceil(std_dev_counts[i])}")
    print(f"Highest Step Count: {math.ceil(max_counts[i])}, Lowest Step Count: {math.ceil(min_counts[i])}")
    print(f"Days with step counts below 5000: {math.ceil(below_5000[i])}, Days with step counts above or equal to 10000: {math.ceil(above_or_equal_10000[i])}")
num_users = data.shape[1]
num_days = data.shape[0]
plt.figure(figsize=(10, 6))
for i in range(num_users):
    plt.bar(np.arange(num_days) + i * 0.2, data[:, i], width=0.2, label=f'{names[i]}')
plt.xlabel('Day')
plt.ylabel('Step Count')
plt.title('Daily Step Count of Each User')
plt.legend()
show_graph = input("Do you want to show the graph? (yes/no): ").lower()
if show_graph == 'yes':
    plt.show()
else:
    print("Graph not shown.")