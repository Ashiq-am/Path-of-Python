# import the module
import heapq as hq

# dictionary to be heapified
li_dict = {11: 121, 2: 4, 5: 25, 3: 9}

# List to hold values from dictionary
heap_dict = []

# extract the values from dictionary
for i in li_dict.values():
    heap_dict.append(i)

# heapify the values
hq.heapify(heap_dict)
print("Values of the dict after heapification :", heap_dict)

# list to hold final heapified dictionary
new_dict = []

# mapping and reconstructing final dictionary
for i in range(0, len(heap_dict)):

    # Iterating the oringinal dictionary
    for k, v in li_dict.items():

        if v == heap_dict[i] and (k, v) not in new_dict:
            new_dict.append((k, v))

new_dict = dict(new_dict)

print("Final dictionary :", new_dict)
