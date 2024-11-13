# Python code to demonstrate
# to remove the tuples
# if certain criteria met

# initialising _list
ini_tuple = [('b', 100), ('c', 200), ('c', 45),
             ('d', 876), ('e', 75)]

# printing iniial_tuplelist
print("intial_list", str(ini_tuple))

# removing tuples for condition met
result = []
for i in ini_tuple:
    if i[1] <= 100:
        result.append(i)

    # printing resultant tuple list
print("Resultant tuple list: ", str(result))

