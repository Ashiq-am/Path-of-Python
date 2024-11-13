# importing numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# creating an x sequence
x = np.linspace(5, 15, 35)

# equation of a straigt line
y = 3*x+4

# creating graph space for two graphs
graph, (plot1, plot2) = plt.subplots(1, 2)

# plot1 graph for normal axes
plot1.plot(x, y)
plot1.set_title("Normal Plot")

# plot2 graph for inverted axes
plot2.plot(x, y)
plot2.set_title("Inverted Plot")
plt.xlim(max(x), min(x))
plt.ylim(max(y), min(y))

# display the graph
graph.tight_layout()
plt.show()
