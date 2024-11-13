# Python3 code to demonstrate
# Conditional String Append
# using loop

def append_str(item, boy_str, girl_str):
    if len(item) > 4 and item[-5] == ' ':
        return item + girl_str
    return item + boy_str


# initializing list
test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']

# initializing append string
boy_str = " Boy"
girl_str = " Girl"

# printing original list
print("The original list is : " + str(test_list))

# Conditional String Append
# using loop
res = [append_str(item, boy_str, girl_str) for item in test_list]

# printing result
print("The filtered strings are : " + str(res))
