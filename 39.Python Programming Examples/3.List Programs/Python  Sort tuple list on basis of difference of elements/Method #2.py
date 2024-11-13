# Python code to demonstrate working of
# Sort tuple list on basis of difference of elements
# using sort() + comparator + cmp()

# comparator function
from filecmp import cmp


def diff_sort(ele1, ele2):
	return cmp(ele2[0] - ele2[1], ele1[0] - ele1[1])

# initialize list
test_list = [(1, 4), (6, 5), (8, 10)]

# printing original list
print("The original list : " + str(test_list))

# Sort tuple list on basis of difference of elements
# using sort() + comparator + cmp()
test_list.sort(diff_sort)

# printing result
print("List after sorting by difference : " + str(test_list))
