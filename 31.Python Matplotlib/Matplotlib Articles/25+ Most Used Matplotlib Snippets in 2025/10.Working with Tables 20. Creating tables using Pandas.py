import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Sales': [15000, 20000, 25000],
    'Profit': [3000, 5000, 7000]
}
df = pd.DataFrame(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.axis('tight')
ax.axis('off')

# Create the table from DataFrame
table = pd.plotting.table(ax, df, loc='center', cellLoc='center')

plt.title("Sales Data Table from DataFrame")
plt.show()