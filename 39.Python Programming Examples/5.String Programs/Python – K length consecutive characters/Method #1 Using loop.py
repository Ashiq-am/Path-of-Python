# Python3 code to demonstrate working of
# K length consecutive characters
# Using loop

# initializing string
test_str = 'geekforgeeekssss is bbbbest forrrr geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

res = []
curr, cnt = None, 0
for chr in test_str:

    # increment for similar character
    if chr == curr:
        cnt += 1
    else:
        curr, cnt = chr, 1

    # if count exactly K, element is added
    if cnt == K:
        res.append(K * chr)

    # printing result
print("The K length similar characters : " + str(res))
