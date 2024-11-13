from itertools import permutations


a = "GeEK"

# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(a)

# Print the obtained permutations
for j in list(p):
	print(j)
