# Python code to split a list into
# sublists of given length.
from itertools import accumulate

# Input list initialization
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list of length in which we have to split
length_to_split = [2, 2, 3, 3]

# Using islice
Output = [Input[x - y: x] for x, y in zip(
		accumulate(length_to_split), length_to_split)]

# Printing Output
print("Initial list is:", Input)
print("Split length list: ", length_to_split)
print("List after splitting", Output)
