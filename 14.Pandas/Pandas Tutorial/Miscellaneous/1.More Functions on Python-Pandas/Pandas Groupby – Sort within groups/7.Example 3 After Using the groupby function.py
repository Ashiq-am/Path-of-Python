# Using groupby function
grouped = df.groupby(['Type'])['top_speed(mph)'].nlargest()

# using nlargest() function will get the
# largest values of top_speed(mph) within
# groups created
print(grouped)
