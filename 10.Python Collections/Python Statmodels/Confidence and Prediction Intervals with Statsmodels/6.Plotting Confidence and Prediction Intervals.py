# Plot the data
plt.scatter(x, y, label='Data')

plt.plot(x, model.fittedvalues, color='red', label='Fitted Line')
plt.fill_between(x, ci_lower, ci_upper, color='red', alpha=0.3, label='95% CI')
plt.fill_between(x, pi_lower, pi_upper, color='blue', alpha=0.2, label='95% PI')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
