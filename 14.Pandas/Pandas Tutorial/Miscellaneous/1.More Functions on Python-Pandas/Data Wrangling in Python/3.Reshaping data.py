# Categorize gender
df['Gender'] = df['Gender'].map({'M': 0,
								'F': 1, }).astype(float)

# Display data
df
