# Python3 code to demonstrate working of
# Double Split String to Matrix
# Using split() + loop

# initializing string
test_str = 'Gfg,best#for,all#geeks,and,CS'

# printing original string
print("The original string is : " + str(test_str))

# initializing row split char
row_splt = "#"

# initializing element split char
ele_splt = ","

# split for rows
temp = test_str.split(row_splt)
res = []

for ele in temp:
    # split for elements
    res.append(ele.split(ele_splt))

# printing result
print("String after Matrix conversion : " + str(res))
