# values to be present in selected rows
li = ['Albert', 'Louis', 'John']

# selecting rows from dataframe
df[(df.points > 50) & (~df.name.isin(li))]
