# importing packages
import seaborn
import matplotlib.pyplot as plt

# loading dataset using seaborn
df = seaborn.load_dataset('tips')

# pairplot with hue sex
seaborn.pairplot(df, hue ='size')
plt.show()
