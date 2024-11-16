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
ax.set_xlabel('X Axis Label', fontsize=14, fontweight='bold')
ax.set_ylabel('Y Axis Label', fontsize=14, fontweight='bold')
plt.show()
