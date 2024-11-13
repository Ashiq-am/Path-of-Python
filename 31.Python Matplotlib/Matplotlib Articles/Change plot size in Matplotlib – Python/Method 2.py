import matplotlib.pyplot as plt

# values on x and y axis
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# plot in it's default size
display(plt.plot(x, y))

# changing the size of figure to 2X2
plt.figure(figsize=(2, 2))
display(plt.plot(x, y))
