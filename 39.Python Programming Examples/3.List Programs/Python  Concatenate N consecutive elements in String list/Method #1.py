# Python3 code to demonstrate working of
# Consecutive N concatenation in String list
# using format() + zip() + iter() + list comprehension

# initialize list
test_list = ['gfg', 'is', 'good', 'for', 'geek', 'people']

# printing original list
print("The original list : " + str(test_list))

# initialize N
N = 3

# Consecutive N concatenation in String list
# using format() + zip() + iter() + list comprehension
temp = '{} ' * N
res = [temp.format(*ele) for ele in zip(*[iter(test_list)] * N)]

# printing result
print("List after N concatenation of String : " + str(res))
