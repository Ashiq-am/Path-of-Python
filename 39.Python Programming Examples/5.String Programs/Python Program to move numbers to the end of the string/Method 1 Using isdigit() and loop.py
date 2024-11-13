# initializing string
test_str = 'geek2eeks4g1eek5sbest6forall9'

# printing original string
print("The original string is : " + str(test_str))

# getting all numbers and removing digits
res = ''
dig = ''
for ele in test_str:
	if ele.isdigit():
		dig += ele
	else:
		res += ele

# adding digits at end
res += dig

# printing result
print("Strings after digits at end : " + str(res))
