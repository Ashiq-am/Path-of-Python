# Python code to demonstrate
# find average of similar tuples in list

# initialising list of tuples
ini_list = [('Akshat', 10), ('Garg', 10), ('Akshat', 2),
							('Garg', 9), ('Akshat', 10)]

# finding average of similar entries
def avg(l):
	return sum(l)/len(l)

result = [(n, avg([v[1] for v in ini_list
				if v[0] is n])) for n in set([n[0] for n in ini_list])]

# printing result
print ("Resultant list of tuples: {}".format(result))
