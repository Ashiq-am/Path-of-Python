import pandas as pd
data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],'Population': [8419600, 3980400, 2716000],
    'Area': [783.8, 503, 589]
}
df = pd.DataFrame(data)

# Setting 'City' column as the index
df.set_index('City', inplace=True)

# Accessing the index
print("\nIndex after setting:")
print(df.index)
print(df)