# Importing Libraries
import matplotlib
import matplotlib.pyplot as plt

# We are just using 10 values
# for our Dataset

# Here, dataset_0 will be constant
# as it's range is just 1 - 10
# But, dataset_1 will be scaled down
# as it's range is 1 - 95,000

global dataset_0, dataset_1
dataset_0 = [10, 5, 6, 1, 3, 7, 9, 4, 8, 2]
dataset_1 = [1, 99, 789, 5, 6859, 541,
			94142, 7, 50826, 35464]

n = len(dataset_1)
mean_ans = 0
ans = 0
j = 0
