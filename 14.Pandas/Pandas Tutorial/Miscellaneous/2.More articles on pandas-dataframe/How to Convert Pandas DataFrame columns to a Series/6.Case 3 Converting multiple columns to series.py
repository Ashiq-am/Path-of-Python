# Converting multiple columns
# i.e 'September' and 'October' to Series
ser1 = df.ix[:,1]
ser2 = df.ix[:,2]

print("\nMultiple columns as a Series:\n")
print(ser1)
print()
print(ser2)

# Checking type
print(type(ser1))
print(type(ser2))
