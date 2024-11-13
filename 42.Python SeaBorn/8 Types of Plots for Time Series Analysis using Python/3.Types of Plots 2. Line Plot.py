# Line plot
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 5))
plt.plot(data)
plt.xlabel('Date')
plt.ylabel('Number of Sunspots')
plt.title('Monthly Sunspots Line Plot')
plt.grid(True)
plt.show()
