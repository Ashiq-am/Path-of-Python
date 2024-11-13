# Python3 code to demonstrate working of
# Convert String to N chunks tuple
# Using zip() + iter() + join()+ list comprehension

# initialize string
test_string = "ggggffffgggg"

# printing original string
print("The original string : " + str(test_string))

# initialize N
N = 4

# Convert String to N chunks tuple
# Using zip() + iter() + join() + list comprehension
res = tuple([''.join(ele) for ele in zip(*[iter(test_string)] * N)])

# printing result
print("Chunked String into tuple : " + str(res))
