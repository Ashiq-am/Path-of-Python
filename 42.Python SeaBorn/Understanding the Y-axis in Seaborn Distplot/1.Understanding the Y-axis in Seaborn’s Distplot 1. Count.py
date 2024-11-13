import seaborn as sns
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sns.distplot(data, kde=False)
plt.show()
