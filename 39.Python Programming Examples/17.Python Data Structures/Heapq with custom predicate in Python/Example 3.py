#import module
import heapq as hq

# the dictionary to be as heap
my_dict = {'z': 'zebra', 'b': 'ball', 'w': 'whale',
		'a': 'apple', 'm': 'monkey', 'c': 'cat'}

# conversion to tuple
my_list = [(k, v) for k, v in my_dict.items()]

print("Before organizing as heap :", my_list)

# arrange as min-heap
hq.heapify(my_list)

print("After organizing as heap :", my_list)

# re convert to dictionary
my_dict = dict(my_list)

print("Resultant dictionary :", my_dict)
