for row in range(0, len(df)):
    df.iat[row, index_total] = df.iat[row,
                                      index_selling] + df.iat[row, index_cost]

    if df.iat[row, index_selling] > df.iat[row, index_cost]:
        df.iat[row, index_max] = df.iat[row, index_selling]
    else:
        df.iat[row, index_max] = df.iat[row, index_cost]
df
