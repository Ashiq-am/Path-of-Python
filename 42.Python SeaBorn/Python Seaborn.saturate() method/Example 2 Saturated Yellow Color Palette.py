import seaborn as sns
import matplotlib.pyplot as plt

saturated_yellow = sns.saturate("yellow")

# Visualize the color palette using palplot
sns.palplot(saturated_yellow)
plt.title('Saturated Yellow Color Palette')
plt.show()
