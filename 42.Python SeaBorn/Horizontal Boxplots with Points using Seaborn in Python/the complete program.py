# Import required modules
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# To avoid changing values everytime you run the cell
np.random.seed(42)


# Creating Data
df = pd.DataFrame({
	'Ice-cream': np.random.normal(40, 15, 100),
	'Chocolate': np.random.normal(60, 10, 100),
	'Cakes': np.random.normal(80, 5, 100)
})


# Using melt dataframe for Converting data to long form
data_df = df.melt(var_name='Dessert', value_name='Votes')


# Adjust size
plt.figure(figsize=(8.3, 6))


# Assign title
plt.title('Horizontal Boxplots with Points using Seaborn')


# Illustrating box plot
sns.boxplot(y="Dessert", x="Votes", data=data_df)
