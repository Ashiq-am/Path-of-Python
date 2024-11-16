import pandas as pd

# Load the Titanic dataset
url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())
