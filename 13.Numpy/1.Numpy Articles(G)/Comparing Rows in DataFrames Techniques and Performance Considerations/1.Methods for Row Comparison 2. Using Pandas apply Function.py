def find_similar_rows(row, df):
    return df[(df['Payee Name'] == row['Payee Name']) &
              (abs(df['Amount'] - row['Amount']) <= 0.1 * row['Amount'])].index.tolist()

results = df.apply(lambda row: find_similar_rows(row, df), axis=1)
print(results)
