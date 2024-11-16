# import the random module
import random


# user defined function to shuffle
def sample_function():
	return 0.5

sample_list = ['A', 'B', 'C', 'D', 'E']
print("Original list : ")
print(sample_list)

# as sample_function returns the same value
# each time, the order of shuffle will be the
# same each time
random.shuffle(sample_list, sample_function)
print("\nAfter the first shuffle : ")
print(sample_list)

sample_list = ['A', 'B', 'C', 'D', 'E']

random.shuffle(sample_list, sample_function)
print("\nAfter the second shuffle : ")
print(sample_list)
