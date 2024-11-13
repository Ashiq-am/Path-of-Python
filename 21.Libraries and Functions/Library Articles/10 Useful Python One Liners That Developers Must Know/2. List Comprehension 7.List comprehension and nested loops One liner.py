x = [1, 2, 3]
y = [4, 5, 6]

coordinates = [(xcor, ycor) for xcor in x for ycor in y]
print(coordinates)

#Output [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
