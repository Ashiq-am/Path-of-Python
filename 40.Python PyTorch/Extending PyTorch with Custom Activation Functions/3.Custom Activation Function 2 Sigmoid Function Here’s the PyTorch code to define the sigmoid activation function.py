import matplotlib.pyplot as plt

# create custom dataset
x = torch.linspace(-10, 10, 100)
k = sigmoid()
y = k(x)

# Plot the sigmoid function
plt.plot(x, y)
plt.grid(True)
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
