import matplotlib.pyplot as plt

# setting font sizeto 30
plt.rcParams.update({'font.size': 30})

x = [1, 2, 3, 4, 5, 6]
y = [0, 2, 4, 6, 8, 10]

# plotting a plot
plt.plot(x, y)

# setting title name
plt.title("Title")

# setting x axis label
plt.xlabel("x axis")

# setting y axis label
plt.ylabel("y axis")

plt.show()
