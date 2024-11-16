import numpy as np

# Create a dictionary to store the data
data = {
    'Sample_1': np.array([0.1, 0.2, 0.3]),
    'Sample_2': np.array([0.4, 0.5, 0.6, 0.7]),
    'Sample_3': np.array([0.8, 0.9]),
    # Add more samples as needed
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Display the DataFrame
print(df)
