# sort the data by values based on column 2
rdd.sortBy(lambda x: x[2]).collect()
