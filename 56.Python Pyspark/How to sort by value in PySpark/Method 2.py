# sort values based on
# column 1 using takeOrdered function
print(rdd.takeOrdered(3,lambda x: x[0]))

# sort values based on
# column 3 using takeOrdered function
print(rdd.takeOrdered(3,lambda x: x[2]))
