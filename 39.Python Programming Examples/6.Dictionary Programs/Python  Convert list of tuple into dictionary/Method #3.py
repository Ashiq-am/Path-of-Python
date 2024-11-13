#Python code to convert list of tuple into dictionary showing
#relation of every element from first list to every other element in the list.

#Importing
from itertools import groupby
from operator import itemgetter

#List initialization
indices = ['x','y','z','w','t','r']
relation =[('x', 'y'), ('x', 'z'), ('x', 'w'), ('y', 'z'), ('y', 'w'), ('z', 'w')]

#Using itertools.groupby and maps
edge = relation + [tuple(reversed(pair)) for pair in relation]
st = itemgetter(0)
end = itemgetter(1)
groups = groupby(sorted(edge), key=st)
mapping = {vertex: list(map(end, edges)) for vertex, edges in groups}
from collections import defaultdict

#Output list
Output = defaultdict(list, mapping)
Output = dict(mapping)
Output.update({vertex: [] for vertex in indices if vertex not in mapping})

#Printing
print("Initial list of tuple is :")
print(relation)
print("Converted dictionary of list :")
print(Output)
