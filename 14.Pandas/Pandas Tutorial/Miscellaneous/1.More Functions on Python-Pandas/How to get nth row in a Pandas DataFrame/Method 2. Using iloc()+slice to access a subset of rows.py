import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],'B': [5, 6, 7, 8],'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Access the 2nd and 3rd rows and the 3rd column
result = df.iloc[1:3, 2]
print(result)