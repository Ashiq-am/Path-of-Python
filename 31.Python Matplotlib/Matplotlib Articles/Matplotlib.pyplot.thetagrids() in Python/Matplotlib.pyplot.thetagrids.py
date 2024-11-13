import matplotlib.pyplot as plt
import numpy as np

employee = ["Rahul", "Joy", "Abhishek",
            "Tina", "Sneha"]

actual = [41, 57, 59, 63, 52, 41]
expected = [40, 59, 58, 64, 55, 40]

# Initialing the spiderplot by
# setting figure size and polar
# projection
plt.figure(figsize=(10, 6))
plt.subplot(polar=True)

theta = np.linspace(0, 2 * np.pi, len(actual))

# Arranging the grid into number
# of sales into equal parts in
# degrees
lines, labels = plt.thetagrids(range(0, 360, int(360 / len(employee))),
                               (employee))

# Plot actual sales graph
plt.plot(theta, actual)
plt.fill(theta, actual, 'b', alpha=0.1)

# Plot expected sales graph
plt.plot(theta, expected)

# Add legend and title for the plot
plt.legend(labels=('Actual', 'Expected'),
           loc=1)
plt.title("Actual vs Expected sales by Employee")

# Dsiplay the plot on the screen
plt.show()
