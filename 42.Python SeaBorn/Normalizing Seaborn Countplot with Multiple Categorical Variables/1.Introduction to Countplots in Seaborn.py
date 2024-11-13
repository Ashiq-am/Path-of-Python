import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load sample dataset
tips = sns.load_dataset("tips")

# Countplot with multiple categorical variables (day and sex)
sns.countplot(x="day", hue="sex", data=tips)
plt.show()
