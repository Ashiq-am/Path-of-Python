# Initial parameters are randomly
# chosing in the range: [-10,10]
parameters = (2*np.random.random(3) - 1)*10

plt.title("Before training")

# Compare true and predicted values before
# training
plt.plot(X, polynomial(parameters, X), "bo")
plt.plot(X, Y, 'go')
plt.legend(["predicted value", "true value"])
plt.show()
