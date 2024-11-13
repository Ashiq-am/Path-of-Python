my_num = 9

# converting number to string and then applying zfill function
num_to_str= str(my_num)
# format my_num to fixed width of 3
result=num_to_str.zfill(3)
print(result)

# format my_num to fixed width of 5
result = num_to_str.zfill(5)
print(result)
