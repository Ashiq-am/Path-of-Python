# Python3 code to demonstrate working of
# Distinct Positive Integers Sum to K
# Using loop

# initializing K
K = 19

# printing K
print("The value of K : " + str(K))

res = []
idx = 0
for ele in range(1, K):
    idx += ele

    # checking for last element point
    if K - idx < ele + 1:
        # appending initial elements
        res.extend(list(range(1, ele)))

        # appending last element left
        res.append(K - idx + ele)
        break

# printing result
print("The Required elements : " + str(res))
