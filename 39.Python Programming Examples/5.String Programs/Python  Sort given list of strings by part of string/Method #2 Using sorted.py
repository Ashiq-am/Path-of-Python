# Python code to demonstrate to sort list
# containing string by part of string

# Initialising list
ini_list = ["GeeksForGeeks abc", "manjeet xab", "akshat bac"]

# printing initial list
print("initial list", str(ini_list))

# code to sort list
res = sorted(ini_list, key=lambda x: x.split()[1])

# printing result
print("result", res)
