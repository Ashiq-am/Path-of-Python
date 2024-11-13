# Python3 code to demonstrate working of
# Maximum value assignment in Nested Dictionary
# Using Counter().most_common() + items() + loop
from collections import Counter

# initializing dictionary
test_dict = {'Manjeet': {'Maths': 1, 'English': 0, 'Physics': 2, 'Chemistry': 3},
             'Akash': {'Maths': 0, 'English': 0, 'Physics': 3, 'Chemistry': 2},
             'Nikhil': {'Maths': 4, 'English': 2, 'Physics': 2, 'Chemistry': 3},
             'Akshat': {'Maths': 1, 'English': 0, 'Physics': 2, 'Chemistry': 0}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Maximum value assignment in Nested Dictionary
# Using Counter().most_common() + items() + loop
res = []
for key, val in test_dict.items():
    cnt = Counter(val)
    res.append({key: cnt.most_common(1)[0]})

# printing result
print("Maximum element key : " + str(res))
