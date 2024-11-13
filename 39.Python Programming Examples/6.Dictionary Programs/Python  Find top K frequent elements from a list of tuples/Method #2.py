# Python code to find top 'k' frequent element
from operator import itemgetter
from itertools import chain

# Input list initialization
Input =[[('Name', 151)], [('ACe', 400)],
		[('TURN', 210)], [('RED', 1113)],
		[('YELLOW', 1)]]

# k initialization
K = 3

# Finding top 'k' frequent element
# without using collection
Output = sorted(list(chain.from_iterable(Input)),
		key = itemgetter(1), reverse = True)[0:K]

# Printing Output
print("Initial List of tuple is", Input)
print("\nTop 'K' elements are", Output)
