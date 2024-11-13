# initializing list
test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

res = []
vow = "aeiou"
for sub in test_list:

    # check for vowel beginning
    flag = any(sub.startswith(ele) for ele in vow)

    if flag:
        res.append(sub)

    # printing result
print("The extracted words : " + str(res))
