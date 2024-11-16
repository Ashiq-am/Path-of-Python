# Dataframe df has only 4 rows

# if we try to select more than 4 row then will come error
# Cannot take a larger sample than population when 'replace = False'
df1.sample(n = 3, replace = False)
