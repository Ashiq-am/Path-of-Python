import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# Create a boxplot and set the title
sns.boxplot(x='day', y='total_bill', data=tips).set(title='Boxplot of Total Bill by Day')
plt.show()
