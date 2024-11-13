import matplotlib.pyplot as plt

# create custom dataset
x = torch.linspace(-5, 5, 100)
k = Softplus()
y = k(x)

# plot the softplus function graph
plt.plot(x, y)
plt.grid(True)
plt.title('Softplus Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
