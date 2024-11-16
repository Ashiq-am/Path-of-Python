import pandas as pd

# Sample DataFrame
data = {
    'Payee Name': ["John", "John", "John", "Sam", "Sam"],
    'Amount': [100, 30, 95, 30, 30],
    'Payment Method': ['Cheque', 'Electronic', 'Electronic', 'Cheque', 'Electronic'],
    'Payment Reference Number': [1, 2, 3, 4, 5],
    'Payment Date': pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'])
}

df = pd.DataFrame(data)

# Compare each row with all other rows
results = []
for i, row in df.iterrows():
    similar_rows = []
    for j, other_row in df.iterrows():
        if i != j and row['Payee Name'] == other_row['Payee Name'] and abs(row['Amount'] - other_row['Amount']) <= 0.1 * row['Amount']:
            similar_rows.append(j)
    results.append(similar_rows)

print(results)
