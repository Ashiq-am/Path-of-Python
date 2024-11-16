# replace column of one DataFrame with
# the column of another DataFrame
df['second_set'] = df1.replace(df['first_set'],df['second_set'])

display(df)
