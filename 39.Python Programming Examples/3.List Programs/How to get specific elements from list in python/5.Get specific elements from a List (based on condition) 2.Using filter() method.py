a = [10, 20, 30, 40, 50]

# Filter with a lambda function
a1 = list(filter(lambda x: x > 20, a))  # [30, 40, 50]

print(a1)