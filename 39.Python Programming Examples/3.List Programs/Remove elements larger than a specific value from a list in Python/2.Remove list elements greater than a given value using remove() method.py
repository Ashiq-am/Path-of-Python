num_list = [30, 200, 65, 88, 98, 500, 34]

# traver the numbers list
for num in num_list:

    # check if current number in the
    # list is greater than 100
    if num > 100:
        # if true remove number from list
        num_list.remove(num)

# display the num_list after removing the
# values that are greater than 100
print(num_list)
