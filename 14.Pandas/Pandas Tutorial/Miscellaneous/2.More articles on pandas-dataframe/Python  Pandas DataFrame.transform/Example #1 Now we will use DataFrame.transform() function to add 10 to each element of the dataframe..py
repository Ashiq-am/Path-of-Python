# add 10 to each element of the dataframe
result = df.transform(func = lambda x : x + 10)

# Print the result
print(result)
