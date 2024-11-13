# Declaring the list geek
geek = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night']

# In python 2.7, just remove the list keyword
partition = list(zip(*[iter(geek)] * 2))
print(partition)
