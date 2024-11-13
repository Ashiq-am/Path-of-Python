# convert dataframe to rdd
rdd = dataframe.rdd

# convert rdd to tuple
data = rdd.map(tuple)

# display data
data.collect()
