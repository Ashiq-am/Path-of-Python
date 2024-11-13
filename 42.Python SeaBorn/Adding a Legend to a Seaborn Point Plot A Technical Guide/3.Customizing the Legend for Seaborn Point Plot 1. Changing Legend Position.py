import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")

# Point plot with hue
sns.pointplot(data=data, x="island", y="body_mass_g", hue="sex")
plt.legend(loc='center left', title='Sex')
plt.show()
