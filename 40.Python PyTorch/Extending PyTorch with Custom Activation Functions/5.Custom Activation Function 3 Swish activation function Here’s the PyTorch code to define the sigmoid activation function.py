import matplotlib.pyplot as plt

# create custom dataset
x = torch.linspace(-10, 10, 100)
k = SwishActivation()
y = k(x)

# Plot the Swish Activation Function
plt.plot(x, y)
plt.grid(True)
plt.title('Swish Activation Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
