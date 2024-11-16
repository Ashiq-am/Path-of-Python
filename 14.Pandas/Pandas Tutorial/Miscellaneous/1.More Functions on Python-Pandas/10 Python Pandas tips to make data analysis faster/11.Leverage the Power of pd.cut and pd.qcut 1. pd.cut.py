import pandas as pd
# Sample DataFrame with a numerical column
data = {'Values': [5, 12, 18, 25, 32, 40, 50, 60]}
df = pd.DataFrame(data)
# Binning values into discrete intervals using pd.cut
bins = [0, 20, 40, 60]
labels = ['Low', 'Medium', 'High']
df['Binned_Values'] = pd.cut(df['Values'], bins=bins, labels=labels)
# Print the DataFrame
print(df)
