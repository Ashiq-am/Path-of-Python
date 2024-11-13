"""In Python, negative sequence indexes represent positions from the end of the array.
Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3].

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc."""




List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing a element using
# negative indexing
print("Acessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])
