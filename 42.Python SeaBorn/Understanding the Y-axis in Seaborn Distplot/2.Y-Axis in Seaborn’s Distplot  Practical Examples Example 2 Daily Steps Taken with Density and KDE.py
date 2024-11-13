import seaborn as sns
import matplotlib.pyplot as plt

# Example data: Daily steps taken by an individual over a month
daily_steps = [8000, 12000, 15000, 9000, 11000, 13000, 7000, 10000, 8500, 12000,
               9500, 10500, 11500, 14000, 8000, 9500, 11000, 13000, 8000, 10000]

# Create a figure and two subplots
fig, axes = plt.subplots(1, 2, figsize=(10,4))

# Plot histogram with density on the first subplot
sns.histplot(daily_steps, bins=10, stat="density", kde=False, ax=axes[0])
axes[0].set_xlabel('Daily Steps')
axes[0].set_ylabel('Density')
axes[0].set_title('Daily Steps Taken (Density)')

# Plot histogram with KDE overlay on the second subplot
sns.histplot(daily_steps, bins=10, kde=True, ax=axes[1])
axes[1].set_xlabel('Daily Steps')
axes[1].set_ylabel('Density')
axes[1].set_title('Daily Steps Taken with KDE')

plt.tight_layout()
plt.show()
