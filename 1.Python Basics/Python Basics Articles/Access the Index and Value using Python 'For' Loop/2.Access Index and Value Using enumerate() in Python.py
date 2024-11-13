# Method 2: Using enumerate
fruits = ['apple', 'banana', 'orange']

print("Indices and values in list:")

# Use enumerate to get both index and value in the loop
for i,fruit in enumerate(fruits):
	print(f"Index: {i}, value: {fruit}")
