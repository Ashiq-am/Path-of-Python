# importing module
import pandas as pd
import numpy as np
from scipy import stats

# Create a DataFrame
df = pd.DataFrame({
	'Name': ['Monty', 'Anurag', 'Kavya', 'Hunny', 'Saurabh',
			'Shubham', 'Ujjawal', 'Satyam', 'Prity', 'Tanya',
			'Amir', 'donald'],
	'Match1_score': [52, 87, 35, 14, 41, 71, 95, 83, 22, 82, 11, 97],
	'match2_score': [45, 80, 62, 53, 49, 82, 36, 97, 84, 93, 39, 59]})

# Display DataFrame
df
