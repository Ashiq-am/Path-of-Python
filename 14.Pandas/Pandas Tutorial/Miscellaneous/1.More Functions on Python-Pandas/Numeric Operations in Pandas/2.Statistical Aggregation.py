# Creating a DataFrame
data = {'A': [10, 20, 30], 'B': [5, 15, 25]}
df = pd.DataFrame(data)

# Calculating mean for each column
mean_values = df.mean()
print("Mean Values:\n", mean_values)
