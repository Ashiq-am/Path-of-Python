# import modules
import heapq as hq

# dictionary to be heapified
dict_1 = {"yz": 2526, "ab": 12, "cd": 34, "ij": 910, "fg": 67}

# convert dictionary to list of tuples
di = list(dict_1.items())

print("dictionary into list :", di)

# converting into heap
hq.heapify(di)

print("Heapified list of tuples :", di)

# converting heap to dictionary
di = dict(di)

print("Dictionary as heap :", di)
