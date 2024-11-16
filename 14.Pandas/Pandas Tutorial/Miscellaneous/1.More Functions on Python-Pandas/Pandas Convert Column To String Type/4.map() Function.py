import pandas as pd

# Create a sample DataFrame
data = {'NumericColumn': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Define a mapping dictionary for conversion
mapping_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

# Use map() to convert 'NumericColumn' based on the mapping dictionary
df['NumericColumn'] = df['NumericColumn'].map(mapping_dict)

# Check the DataFrame
df.info()
