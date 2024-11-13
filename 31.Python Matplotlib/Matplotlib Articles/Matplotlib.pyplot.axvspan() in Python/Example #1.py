# Importing matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Initializing x and y
x =[1, 15, 27, 48, 50]
y =[1, 12, 22, 45, 67]

# Plotting the graph
plt.plot(x, y)

# Drawing rectangle starting
# x = 5 and extending till x = 20
# With vertical span starting at
# half the length of y-axis(ymin = 0.5)
# And extending till the top of
# axis(ymax = 1)
plt.axvspan(5, 20, ymin = 0.5, ymax = 1)
plt.show()
