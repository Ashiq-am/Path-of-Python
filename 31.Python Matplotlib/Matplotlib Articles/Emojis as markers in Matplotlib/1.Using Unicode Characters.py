# importing matplotlib module
import matplotlib.pyplot as plt

# defining a list of x and v values
x_values = [1, 2, 3, 4, 5]
y_values = [2*x for x in x_values]

# plotting the graph
fig, ax = plt.subplots(figsize=(10, 6))

# check that the marker value is given as
# '$U0001F601$'
ax.plot(x_values, y_values, marker='$\U0001F601$', ms=20, c='green')
ax.set_title('Squared Values', fontsize=15)
ax.set_xlabel('Value')
ax.set_ylabel('Square of Value')
plt.show()
