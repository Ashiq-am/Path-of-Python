# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# making copy of address column
new = df["Address"].copy()

# concatenating address with name column
# overwriting name column
df["Name"] = df["Name"].str.cat(new, sep=", ")

# display
print(df)