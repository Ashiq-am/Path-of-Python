# Import pandas & Numpy package
import numpy as np
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
		'Age':[27, 24, 22, 32, 15],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Chose how many index include for random selection
chosen_idx = np.random.choice(4, replace = True, size = 6)

df2 = df.iloc[chosen_idx]

df2
