import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(mutual_info_df, annot=True, cmap='coolwarm', square=True)
plt.title('Pairwise Mutual Information')
plt.show()
