''''''



'''C-style approach:This approach requires prior knowledge of total number of iterations'''


# A C-style way of accessing list elements
cars = ["Aston", "Audi", "McLaren"]
i = 0
while (i < len(cars)):
	print(cars[i])
	i += 1






"""Important Points:

This style of looping is rarely used by python programmers.
This 4-step approach creates no compactness with single-view looping construct.
This is also prone to errors in large-scale programs or designs.
There is no C-Style for loop in Python, i.e., a loop like for (int i=0; i<n; i++)"""