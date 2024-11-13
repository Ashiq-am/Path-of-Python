""""""



'''Please refer the below code to see the difference. When we assign {} to a dictionary, a new empty 
dictionary is created and assigned to the reference. 

But when we do clear on a dictionary reference, the actual dictionary content is removed, 
so all references referring to the dictionary become empty.'''





# Python code to demonstrate difference
# clear and {}.

text1 = {1: "geeks", 2: "for"}
text2 = text1

# Using clear makes both text1 and text2
# empty.
text1.clear()

print('After removing items using clear()')
print('text1 =', text1)
print('text2 =', text2)

text1 = {1: "one", 2: "two"}
text2 = text1

# This makes only text1 empty.
text1 = {}

print('After removing items by assigning {}')
print('text1 =', text1)
print('text2 =', text2)
