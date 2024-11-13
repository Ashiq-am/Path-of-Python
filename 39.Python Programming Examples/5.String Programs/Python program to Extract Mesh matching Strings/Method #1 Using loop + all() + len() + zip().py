# Python3 code to demonstrate working of
# Extract Mesh matching Strings
# Using len() + loop + zip() + all()

# initializing list
test_list = ["geeks", "best", "peeks", "for", "seeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing mesh
mesh = "_ee_s"

res = []
for sub in test_list:

    # testing for matching mesh, checking each character and length
    if (len(sub) == len(mesh)) and all((ele1 == "_") or (ele1 == ele2)
                                       for ele1, ele2 in zip(mesh, sub)):
        res.append(sub)

    # printing result
print("The extracted strings : " + str(res))
