temp = 'Geeks 22536 for 445 Geeks'
data = [x for x in (int(x) for x in temp if x.isdigit()) if x%2 == 0]
print(data)
