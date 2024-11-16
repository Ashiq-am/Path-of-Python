# rows list initialization
rows = []

# appending rows
for data in list:
    data_row = data['Student']
    time = data['Name']

    for row in data_row:
        row['Name'] = time
        rows.append(row)

    # using data frame
df = pd.DataFrame(rows)

# print(df)
