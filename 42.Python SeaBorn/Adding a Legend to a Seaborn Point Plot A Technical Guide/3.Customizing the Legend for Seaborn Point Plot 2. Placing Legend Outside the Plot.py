import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("penguins")

# Point plot with hue
sns.pointplot(data=data, x="island", y="body_mass_g", hue="sex")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, title='Sex')
plt.show()
