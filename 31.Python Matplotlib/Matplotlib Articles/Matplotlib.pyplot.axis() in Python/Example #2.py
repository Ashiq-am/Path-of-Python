import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]

plt.plot(x, y)

# we can turn off the axis and display
# only the line by passing the
# optional parameter 'off' to it
plt.axis('off')

plt.show()
