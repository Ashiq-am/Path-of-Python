# Python code to demonstrate the
# grouper Recipie
import itertools as it

# defining the grouper function
def grouper(inputs, n, fillvalue = None):
	iters = [iter(inputs)] * n
	return it.zip_longest(*iters, fillvalue = fillvalue)

alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
		'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha, 3)))
