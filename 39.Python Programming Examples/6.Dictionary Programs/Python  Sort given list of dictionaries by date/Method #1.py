# Python code to demonstrate
# sort a list of dictionary
# where value date is in string

# Initialising list of dictionary
ini_list = [{'name': 'akash', 'd.o.b': '1997-03-02'},
            {'name': 'manjeet', 'd.o.b': '1997-01-04'},
            {'name': 'nikhil', 'd.o.b': '1997-09-13'}]

# printing initial list
print("initial list : ", str(ini_list))

# code to sort list on date
ini_list.sort(key=lambda x: x['d.o.b'])

# printing final list
print("result", str(ini_list))
