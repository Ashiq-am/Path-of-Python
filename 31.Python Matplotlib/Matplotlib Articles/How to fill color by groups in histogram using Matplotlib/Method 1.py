# import necessary packages
import pandas as pd
import matplotlib.pyplot as plt

# create a DataFrame
personAges = pd.DataFrame({'Gender': ['Male', 'Female',
									'Male', 'Female',
									'Female'],
						'Age': [25, 19, 21, 30, 18]})

# group data & plot histogram
personAges.pivot(columns='Gender', values='Age').plot.hist()
plt.show()
