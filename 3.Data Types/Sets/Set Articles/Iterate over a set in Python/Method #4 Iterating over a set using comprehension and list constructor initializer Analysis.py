# importing libraires
from timeit import default_timer as timer
import itertools
import random

# Function under evaluation
def test_func(test_set):

	list(val for val in test_set)

# Driver function
if __name__ == '__main__':

	random.seed(21)
	for _ in range(5):
		test_set = set()

		# generating a set of random numbers
		for el in range(int(1e6)):
			el = random.random()
			test_set.add(el)

		start = timer()
		test_func(test_set)
		end = timer()

		print(str(end - start))
