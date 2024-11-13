import matplotlib.pyplot as plt


# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]


# Creating figure object
plt.figure()

# addind first subplot
plt.subplot(121)
plt.plot(x, y)

# addding second subplot
plt.subplot(122)
plt.plot(y, x)
