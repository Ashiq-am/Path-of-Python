#Python code to convert list of tuple into dictionary showing
#relation of every element from first list to every other element in the list.

#Importing
import networkx as nx

#List initialization
indices = ['x','y','z','w','t','r']
relation =[('x', 'y'), ('x', 'z'), ('x', 'w'), ('y', 'z'), ('y', 'w'), ('z', 'w')]

#dictionary initialization
Output = {}

#Using networkx to solve
temp=nx.Graph(relation)
temp.add_nodes_from(indices)
Output = nx.to_dict_of_lists(temp)

#Printing
print("Initial list of tuple is :")
print(relation)
print("Converted dictionary of list :")
print(Output)
