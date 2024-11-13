# import required modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# creating dataset
df = pd.DataFrame({
	'Ice-cream': np.random.normal(57, 5, 100),
	'Chocolate': np.random.normal(73, 5, 100),
	'cupcake': np.random.normal(68, 8, 100),
	'jamroll': np.random.normal(37, 10, 100),
	'cake': np.random.normal(76, 5, 100),

})


# sort on the basis of mean
index_sort = df.mean().sort_values().index

# now applying the sorted indices to the data
df_sorted = df[index_sort]


# plotting the boxplot for the data
sns.boxplot(data = df_sorted)

# Label x-axis
plt.xlabel('Desserts')

# labels y-axis
plt.ylabel('perference of people')
