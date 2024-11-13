import matplotlib.pyplot as plt

x=['one', 'two', 'three', 'four', 'five']

# giving the values against
# each value at x axis
y=[5, 24, 35, 67, 12]
plt.bar(x, y)

# setting x-label as pen sold
plt.xlabel("pen sold")

# setting y_label as price
plt.ylabel("price")
plt.title(" Vertical bar graph")
plt.show()
