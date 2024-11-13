import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

np.random.seed(42)
hours = [f"{hour}:00" for hour in range(24)]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
data = np.random.rand(7, 24) * 60  # Average time spent in minutes

df = pd.DataFrame(data, index=days, columns=hours)

# Define colormap from green (high engagement) to red (low engagement)
cmap = mcolors.LinearSegmentedColormap.from_list("green_red", ["green", "yellow", "red"], N=100)

plt.figure(figsize=(14, 7))
sns.heatmap(df, cmap=cmap, annot=True, fmt=".1f", linewidths=.5)
plt.title("User Engagement on a Website (Minutes Spent)")
plt.xlabel("Hour of the Day")
plt.ylabel("Day of the Week")
plt.show()
