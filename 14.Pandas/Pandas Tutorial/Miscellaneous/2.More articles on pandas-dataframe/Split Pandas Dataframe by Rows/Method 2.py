# splitting dataframe by groups
# grouping by particular dataframe column
grouped = df.groupby(df.color)
df_new = grouped.get_group("E")
df_new
