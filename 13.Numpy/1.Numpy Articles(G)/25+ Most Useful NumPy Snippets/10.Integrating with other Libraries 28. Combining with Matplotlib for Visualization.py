import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Plotting
df.plot(x='A', y='B', kind='line')
plt.title('Line Plot of A vs B')
plt.show()