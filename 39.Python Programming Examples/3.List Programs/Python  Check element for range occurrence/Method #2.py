# Python3 code to demonstrate working of
# Check element for range occurrence
# Using next() + enumerate() + generator expression

# Initializing list
test_list = [(45, 90), (100, 147), (150, 200)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing element
N = 124

# Check element for range occurrence
# Using next() + enumerate() + generator expression
res = next((idx for idx, (sec, fir) in enumerate(test_list) if sec <= N <= fir), None)

# printing result
print("The index of tuple between which element occurs : " + str(res))
