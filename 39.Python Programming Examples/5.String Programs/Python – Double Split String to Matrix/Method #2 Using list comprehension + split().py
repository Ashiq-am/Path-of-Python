# Python3 code to demonstrate working of
# Double Split String to Matrix
# Using list comprehension + split()

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

# using list comprehension as shorthand
res = [ele.split(ele_splt) for ele in temp]

# printing result
print("String after Matrix conversion : " + str(res))
