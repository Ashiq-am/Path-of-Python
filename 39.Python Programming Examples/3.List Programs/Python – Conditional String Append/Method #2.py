# Python3 code to demonstrate
# Conditional String Append
# using list comprehension

# initializing list
test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']

# initializing append string
boy_str = " Boy"
girl_str = " Girl"

# printing original list
print ("The original list is : " + str(test_list))

# Conditional String Append
# using list comprehension
res = [ele + girl_str if ele[-5] == ' ' else ele + boy_str for ele in test_list]

# printing result
print ("The filtered strings are : " + str(res))
