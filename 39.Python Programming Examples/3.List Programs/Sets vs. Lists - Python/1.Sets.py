# Creating a set
s1 = {"apple", "banana", "cherry"}

# Adding an item
s1.add("orange")

# Removing an item (will not raise error if item is not present)
s1.discard("banana")

# Union of two sets
s2 = {"carrot", "potato", "onion"}
s3 = s1.union(s2)

# Intersection of two sets
s4 = s1.intersection(s2)

# Print all sets
print(s1)
print(s2)
print("Union:", s3)
print("Intersection:", s4)