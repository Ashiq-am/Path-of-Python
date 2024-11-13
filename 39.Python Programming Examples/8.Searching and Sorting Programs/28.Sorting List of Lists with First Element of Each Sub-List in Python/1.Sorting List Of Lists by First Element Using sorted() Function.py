# Using the sorted() Function with a Lambda Function
list_of_lists= [[3, 'b'], [1, 'a'], [2, 'c']]
sorted_list= sorted(list_of_lists, key=lambda x: x[0])

#Display the sorted
print(sorted_list)
