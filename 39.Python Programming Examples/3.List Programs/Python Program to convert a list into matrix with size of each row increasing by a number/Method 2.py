# initializing list
test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing N
N = 3

# getting incremented chunks
# using list comprehension as shorthand
res = [test_list[0: (idx + 1) * N] for idx in range(0, len(test_list) // N)]

# printing result
print("Constructed Chunk Matrix : " + str(res))
