# Python code to illustrate expandtabs()
string = 'GEEKS\tFOR\tGEEKS'

# No parameters, by default size is 8
print (string.expandtabs())

# tab size taken as 2
print(string.expandtabs(2))

# tab size taken as 5
print(string.expandtabs(5))
