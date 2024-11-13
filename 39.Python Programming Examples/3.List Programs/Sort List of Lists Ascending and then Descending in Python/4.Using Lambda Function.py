List = [[2, 8, 10], [12, 45, 2], [4, 10, 1]]

List.sort(key=lambda x:x[1])

print("Sorting by 2nd column in Ascending", List)
List.sort(key=lambda x:x[1], reverse=True)
print("Sorting by 2nd column in Descending", List)
