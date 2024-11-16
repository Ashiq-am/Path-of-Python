import pandas as pd

# Example DataFrame with leading zeros
data = {'Value': [0, 0, 0, 1, 0, 3, 0, 0, 5, 0]}
df = pd.DataFrame(data)

# Replace zeros with the previous non-zero value,
# and fill leading zeros with the first non-zero value
df['Value'] = df['Value'].replace(0, pd.NA).ffill()
df['Value'] = df['Value'].replace(0, pd.NA).bfill()

print(df)
