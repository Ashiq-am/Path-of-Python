# ...

for column in df:
    column_length = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    worksheet.set_column(col_idx, col_idx, column_length + 2)
