# create a list of names and marks
list1 = ['sravan', 98, 'harsha', 'jyothika',
         'deepika', 78, 90, 'ramya']

# display
list1

# iterate through list of elemens
for i in list1:

    # check for type is str
    if (type(i) is str):
        # display index
        print(list1.index(i))
