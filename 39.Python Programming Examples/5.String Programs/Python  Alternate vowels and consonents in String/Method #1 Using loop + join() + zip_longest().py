# Python3 code to demonstrate working of
# Alternate vowels and consonents in String
# using zip_longest() + join() + loop
from itertools import zip_longest

# initializing string
test_str = "gaeifgsbou"

# printing original string
print("The original string is : " + test_str)

# Alternate vowels and consonents in String
# using zip_longest() + join() + loop
vowels = ['a', 'e', 'i', 'o', 'u']
test_vow = []
test_con = []
for ele in test_str:
    if ele in vowels:
        test_vow.append(ele)

    elif ele not in vowels:
        test_con.append(ele)

res = ''.join(''.join(ele) for ele in zip_longest(test_vow, test_con, fillvalue =''))

# printing result
print("Alternate consonents vowels are: " + res)
