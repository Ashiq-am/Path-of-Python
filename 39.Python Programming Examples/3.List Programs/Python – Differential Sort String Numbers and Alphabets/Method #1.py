# Python3 code to demonstrate working of
# Differential Sort String Numbers and Alphabets
# Using isnumeric() + loop

# initializing list
test_list = ["1", "G", "7", "L", "9", "M", "4"]

# printing original list
print("The original list is : " + str(test_list))

numerics = []
alphabets = []
for sub in test_list:

    # checking and inserting in respective container
    if sub.isnumeric():
        numerics.append(sub)
    else:
        alphabets.append(sub)

# attaching lists post sort
res = sorted(alphabets) + sorted(numerics)

# printing result
print("The Custom sorted result : " + str(res))
