import os

# To get directories as well as files present
# in a path
list_1 = os.listdir(path=r"root/home/project")
print(list_1)

# To get only files present in a path
list_2 = os.listdir(path=r"root/home/project")

# Loop through each value in the list_2
for val in list_2:

    # Remove the value from list_2 if the "." is
    # not present in value
    if "." not in val:
        list_2.remove(val)
print(list_2)
