# Python3 code to demonstrate working of
# Remove Kth key from dictionary
# Using loop

# initializing dictionary
test_dict = {"Gfg": 20, "is": 36, "best": 100,
             "for": 17, "geeks": 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing size
K = 3

cnt = 0
for key in test_dict:
    cnt += 1

    # delete key if counter is equal to K
    if cnt == K:
        del test_dict[key]
        break

# printing result
print("Required dictionary after removal : " + str(test_dict))
