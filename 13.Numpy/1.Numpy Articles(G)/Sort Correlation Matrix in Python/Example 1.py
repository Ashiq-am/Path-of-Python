# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = sns.load_dataset('iris')

# Convert categorical values to numeric
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Create correlation matrix
corr_mat = df.corr(method='pearson')

# Convert correlation matrix to 1-D Series and sort
sorted_mat = corr_mat.unstack().sort_values()

print(sorted_mat)
