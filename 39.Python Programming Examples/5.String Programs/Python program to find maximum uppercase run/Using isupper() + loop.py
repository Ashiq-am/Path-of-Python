# Python3 code to demonstrate working of
# Maximum uppercase run
# Using isupper() + loop

# initializing string
test_str = 'GeEKSForGEEksISBESt'

# printing original string
print("The original string is : " + str(test_str))

cnt = 0
res = 0
for idx in range(0, len(test_str)):

    # updating run count on uppercase
    if test_str[idx].isupper():
        cnt += 1

    # on lowercase, update the maxrun
    else:
        res = cnt
        cnt = 0
if test_str[len(test_str) - 1].isupper():
    res = cnt

# printing result
print("Maximum Uppercase Run : " + str(res))
