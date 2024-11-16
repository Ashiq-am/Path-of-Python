# replaceing value of DataFrame
df1.first_set[df1.first_set == '66'] = 'DF1'
df2.first_set[df2.first_set == 'g'] = 'DF2'

# display updated table
display(df1)
display(df2)
