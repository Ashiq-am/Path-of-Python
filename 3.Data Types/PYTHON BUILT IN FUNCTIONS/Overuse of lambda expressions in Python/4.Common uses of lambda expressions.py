# Python program showing use
# of lambda function

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sort_lambda = sorted(nums, key = lambda x: x%2)
print(sort_lambda)
