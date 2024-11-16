import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'A': [1, 3, 5, 7],
    'B': [2, 4, 6, 8]
}
df = pd.DataFrame(data)

# Plot
ax = df.plot()
ax.set_xlabel('X Axis Label')
ax.set_ylabel('Y Axis Label')

# Rotate x-axis labels
ax.set_xticks(ax.get_xticks())  # Ensure rotation is applied to all ticks
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.show()
