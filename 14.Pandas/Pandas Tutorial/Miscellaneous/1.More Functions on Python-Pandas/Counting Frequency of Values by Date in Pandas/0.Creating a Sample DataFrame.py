import pandas as pd

data = {
    'date': ['2024-09-01', '2024-09-01',
             '2024-09-02', '2024-09-02',
             '2024-09-03', '2024-09-03',
             '2024-09-03'],
    'value': ['A', 'B', 'A', 'C', 'A', 'B', 'B']
}

df = pd.DataFrame(data)
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])
print(df)
