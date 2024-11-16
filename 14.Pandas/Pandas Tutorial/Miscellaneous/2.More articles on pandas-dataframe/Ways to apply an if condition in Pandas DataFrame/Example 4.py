# If condition on a cell value using iloc() or loc() functions
# iloc() is based on index search and loc() based on label search

# using iloc()
if df.iloc[2, 1] > 1500:
    print("Badminton Price > 1500")
else:
    print("Badminton Price < 1500")

# using loc()
print(df.loc[2, 'MRP'])
if df.iloc[2, 'MRP'] > 1500:
    print("Badminton Price > 1500")
else:
    print("Badminton Price < 1500")
