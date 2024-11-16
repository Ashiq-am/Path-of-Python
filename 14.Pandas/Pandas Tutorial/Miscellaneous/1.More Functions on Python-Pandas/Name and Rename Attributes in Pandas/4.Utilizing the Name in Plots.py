# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame
df = pd.DataFrame({
	'Age': [28, 35, 42, 99, 87],
	'Name': ['Allen', 'Ravindra', 'Henry', 'Keshav', 'Shami']
})

# Extracting the 'Age' column
age_series = df['Age']

# Renaming the Series
renamed_series = age_series.rename("Ages")

# Plotting the Series
age_series.plot(kind='bar')

# Set the title
plt.title("Ages of Individuals")

# Plotting values of age_series
plt.ylabel(age_series.name)

# Plot the graph
plt.show()
