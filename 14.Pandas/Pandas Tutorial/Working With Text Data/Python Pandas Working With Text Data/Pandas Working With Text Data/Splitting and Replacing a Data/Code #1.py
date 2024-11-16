# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# dropping null value columns to avoid errors
df.dropna(inplace=True)

# new data frame with split value columns
df["Address"] = df["Address"].str.split("a", n=1, expand=True)

# df display
print(df)