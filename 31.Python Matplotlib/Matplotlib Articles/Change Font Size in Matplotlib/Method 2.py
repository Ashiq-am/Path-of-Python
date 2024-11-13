import matplotlib.pyplot as plt


# creating a dictionary
font = {'size': 10}

# using rc function
plt.rc('font', **font)

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
