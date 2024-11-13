# initializing string
test_str = 'geek2eeks4g1eek5sbest6forall9'

# printing original string
print("The original string is : " + str(test_str))

# getting all numbers
dig = ''.join(ele for ele in test_str if ele.isdigit())

# getting all elements not digit
res = ''.join(ele for ele in test_str if not ele.isdigit())

# adding digits at end
res += dig

# printing result
print("Strings after digits at end : " + str(res))
