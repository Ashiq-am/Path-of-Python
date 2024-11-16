# Training with SPSA
parameters = SPSA(LossFunction = lambda parameters: Loss(parameters, X, Y),
				parameters = parameters)

plt.title("After training")
plt.plot(X, polynomial(parameters, X), "bo")
plt.plot(X, Y, 'go')
plt.legend(["predicted value", "true value"])
plt.show()
