# Python code to demonstrate flattening a list of lists
import itertools as it

list_of_lists = [[1, 2], [3, 4]]
chain_object = it.chain.from_iterable(list_of_lists)

# Return chain object with nested lists separated
# Convert to list to flatten
flattened_list = list(chain_object)

print(flattened_list)
