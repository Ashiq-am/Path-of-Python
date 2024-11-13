import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
ax = sns.boxplot(x='day', y='total_bill', data=tips)

# Set the title using set_title
ax.set_title('Boxplot of Total Bill by Day')
plt.show()
