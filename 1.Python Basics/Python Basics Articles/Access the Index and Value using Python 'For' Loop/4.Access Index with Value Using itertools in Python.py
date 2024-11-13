from itertools import count

# Sample list
fruits = ['apple', 'banana', 'orange']

# Create an iterator that produces consecutive integers starting from 0
index_counter = count()

# Use zip to combine the index_counter with the list elements
for i, fruit in zip(index_counter, fruits):
    print(f"Index: {i}, Value: {fruit}")
