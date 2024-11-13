# sort the data by values based on column 1
rdd.sortBy(lambda x: x[0]).collect()
