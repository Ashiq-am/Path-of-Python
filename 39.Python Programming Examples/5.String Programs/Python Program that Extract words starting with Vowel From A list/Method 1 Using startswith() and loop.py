# initializing list
test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

res = []
vow = "aeiou"
for sub in test_list:
    flag = False

    # checking for begin char
    for ele in vow:
        if sub.startswith(ele):
            flag = True
            break
    if flag:
        res.append(sub)

    # printing result
print("The extracted words : " + str(res))
