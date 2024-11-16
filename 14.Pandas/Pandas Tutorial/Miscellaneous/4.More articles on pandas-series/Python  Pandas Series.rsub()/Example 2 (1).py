# perform reverse subtraction with 1000
# fill 100 at the place of all missing values
selected_items = sr.rsub(other = 1000, fill_value = 100)

# Print the returned Series object
print(selected_items)
