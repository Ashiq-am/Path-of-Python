import pandas as pd

# Sample DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-02',
             '2024-01-03', '2024-01-04',
             '2024-01-05', '2024-01-06',
             '2024-01-07', '2024-01-08',
             '2024-01-09', '2024-01-10'],
    'Value': [10, 4, 0, 0, 30, 0, 7, 0, 0, 0]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

print(df)
