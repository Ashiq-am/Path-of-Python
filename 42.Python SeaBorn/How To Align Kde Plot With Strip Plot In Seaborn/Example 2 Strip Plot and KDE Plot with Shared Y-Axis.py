import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot a strip plot
sns.stripplot(x="day", y="total_bill", data=data, ax=ax1, jitter=True, color="blue", alpha=0.6)
# Create a twin axis sharing the same y-axis
ax2 = ax1.twinx()
# Plot a KDE plot on the twin axis
days = data['day'].unique()
for day in days:
    subset = data[data['day'] == day]
    sns.kdeplot(subset['total_bill'], ax=ax2, label=day, fill=True, alpha=0.4)
plt.show()
