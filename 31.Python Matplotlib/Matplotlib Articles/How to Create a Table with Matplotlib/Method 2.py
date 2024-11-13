# import packages and modules
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import table

# loading the iris dataset
iris = load_iris()

# creating a 2 dimensional dataframe out of the given data
iris_df = pd.DataFrame(data=np.c_[iris['data'],
								iris['target']],
					columns=iris['feature_names'] + ['target'])

# grouping data and calculating average
grouped_dataframe = iris_df.groupby('target').mean().round(1)
grouped_dataframe['species_name'] = ['setosa', 'versicolor', 'virginica']

# plotting data
ax = plt.subplot(211)
plt.title("Iris Dataset Average by Plant Type")
plt.ylabel('Centimeters (cm)')

ticks = [4, 8, 12, 16]
a = [x - 1 for x in ticks]
b = [x + 1 for x in ticks]

plt.xticks([])

plt.bar(a, grouped_dataframe.loc[0].values.tolist()[
		:-1], width=1, label='setosa')
plt.bar(ticks, grouped_dataframe.loc[1].values.tolist()[
		:-1], width=1, label='versicolor')
plt.bar(b, grouped_dataframe.loc[2].values.tolist()[
		:-1], width=1, label='virginica')

plt.legend()
plt.figure(figsize=(12, 8))
table(ax, grouped_dataframe.drop(['species_name'], axis=1), loc='bottom')
