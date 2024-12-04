a = [1, 2, 3, 6, 7, 8, 6]

 # Make a copy of the list to avoid skipping items
for x in a[:]:
    if x == 6:
        a.remove(x)
print(a)