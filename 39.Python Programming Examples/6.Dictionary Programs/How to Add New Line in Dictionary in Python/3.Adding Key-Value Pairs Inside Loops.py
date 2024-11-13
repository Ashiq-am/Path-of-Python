# Initializing an empty dictionary
my_dict = {}

# Adding key-value pairs dynamically inside a loop
for i in range(5):
    key = f"item_{i}"
    value = i * 10
    my_dict[key] = value

print(my_dict)
