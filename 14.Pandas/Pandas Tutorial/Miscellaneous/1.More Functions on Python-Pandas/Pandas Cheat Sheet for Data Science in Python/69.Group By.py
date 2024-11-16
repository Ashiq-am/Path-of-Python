# Group the DataFrame by 'Origin' column
grouped = df.groupby(by='Origin')

# Compute the sum as per Origin State
# All the above function can be
# applied here like median, std etc
print(grouped.agg(['sum', 'mean']))
