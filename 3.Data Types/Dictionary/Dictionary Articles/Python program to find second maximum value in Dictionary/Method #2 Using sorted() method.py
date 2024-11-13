# Python code to find second largest
# element from a dictionary using sorted() method

# creating a new Dictionary
example_dict = {"mark": 13, "steve": 3, "bill": 6, "linus": 11}

# now directly print the second largest
# value in the dictionary
print("Output1:", sorted(example_dict.values())[-2])

# More than 1 keys with maximum value are present
example_dict = {"fb": 20, "whatsapp": 12, "instagram": 20, "oculus": 10}
print("Output2:", sorted(set(example_dict.values()), reverse=True)[-2])
