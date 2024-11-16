# Reset the indexes to default
# inplace = True will make changes to the orginal dataframe
# drop =True will drop the initial indexes
df.reset_index(drop=True, inplace=True)
print(df)
