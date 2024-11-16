# match the indexes
# fill the unmatched index using 'ffill' method
# maximum consecutive unmatched indexes to be filled is 1

df.reindex_like(df1, method ='ffill', limit = 1)
