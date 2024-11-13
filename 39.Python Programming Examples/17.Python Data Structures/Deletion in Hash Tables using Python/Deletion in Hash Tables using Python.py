# Creating a hash table
hash_table = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Deleting an element from the hash table
delete_key = 'B'
if delete_key in hash_table:
    del hash_table[delete_key]
    print("Key '{}' deleted successfully.".format(delete_key))
else:
    print("Key '{}' not found in the hash table.".format(delete_key))

# Displaying the updated hash table
print("Updated hash table:", hash_table)
