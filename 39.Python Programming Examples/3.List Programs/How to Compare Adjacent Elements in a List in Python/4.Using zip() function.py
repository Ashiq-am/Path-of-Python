def compare(my_list):
    #getting all the pairs and iterating over them
    for i, j in zip(my_list, my_list[1:]):
        #displaying the result
        print (i,j," ",i==j)

# number list
compare([1, 2, 2, 3, 4, 4, 5])
