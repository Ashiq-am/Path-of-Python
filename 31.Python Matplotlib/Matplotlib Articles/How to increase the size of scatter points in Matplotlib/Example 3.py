import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.figure(figsize=(10, 10))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3*i+2 for i in x]
size = [n*100 for n in range(1, len(x)+1)]
# print(size)

plt.scatter(x, y, s=size, c='g')
plt.title("Scatter Plot with increase in size of scatter points ", fontsize=22)

plt.xlabel('X-axis', fontsize=20)
plt.ylabel('Y-axis', fontsize=20)

plt.xticks(x, fontsize=12)
plt.yticks(y, fontsize=12)

plt.show()
