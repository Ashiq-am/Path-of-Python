# Declaring both the lists
list1 = ["a","b","c","d"]
list2 = ["a","b"]

intersection_set = set(list1).intersection(set(list2))

if len(intersection_set)==len(list2):
	print("Elements of list2 exists in list1")
