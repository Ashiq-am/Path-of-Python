# define a list
l = []

# collect data from the dataframe
for i in dataframe.collect():
    l.append(tuple(i))
# convert to tuple and append to list

# print list of data
print(l)
