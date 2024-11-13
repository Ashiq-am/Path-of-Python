import random

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
print("The original list is : " + str(test_list))

# generating random row index
row_index = random.randint(0, len(test_list)-1)

# extracting the row corresponding to the random index using list comprehension
row = [test_list[row_index][i] for i in range(len(test_list[row_index]))]

# getting a sample of elements from the row using random.sample()
sample = random.sample(row, k=1)

# getting the randomly selected element from the sample
res = sample[0]

# printing result
print("Random number from Matrix Row : " + str(res))
