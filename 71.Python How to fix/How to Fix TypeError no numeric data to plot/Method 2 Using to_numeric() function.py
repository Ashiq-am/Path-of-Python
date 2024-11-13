# importing pandas
import pandas as pd
# importing numpy
import numpy as np
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

petal_length = ['3.3', '3.5', '4.0', '4.5',
				'4.6', '5.0', '5.5', '6.0',
				'6.5', '7.0']
petal_width = ['3.6', '3.8', '4.4', '6.6',
			'6.8', '7.0', '7.5', '8.0',
			'8.5', '8.9']


df = pd.DataFrame({'petal_length(cm)': petal_length,
				'petal_width(cm)': petal_width})
# Using to_numeric() function
df['petal_length(cm)'] = pd.to_numeric(df['petal_length(cm)'])
df['petal_width(cm)'] = pd.to_numeric(df['petal_width(cm)'])

df.plot(x='petal_length(cm)', y='petal_width(cm)')
plt.show()
