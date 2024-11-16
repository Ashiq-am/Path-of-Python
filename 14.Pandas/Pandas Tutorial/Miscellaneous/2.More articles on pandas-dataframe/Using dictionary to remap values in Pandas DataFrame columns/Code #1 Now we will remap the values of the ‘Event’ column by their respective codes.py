# Create a dictionary using which we
# will remap the values
dict = {'Music' : 'M', 'Poetry' : 'P', 'Theatre' : 'T', 'Comedy' : 'C'}

# Print the dictionary
print(dict)

# Remap the values of the dataframe
df.replace({"Event": dict})
