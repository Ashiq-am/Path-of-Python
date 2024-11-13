# Custom function to calculate standard deviation
def custom_error(data):
    return np.std(data)

# Barplot with error bars based on standard deviation
sns.barplot(x='Category', y='Values', data=data, ci='sd')
plt.show()
