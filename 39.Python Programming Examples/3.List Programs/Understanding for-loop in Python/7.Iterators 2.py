numList = [0, 2, 4]

# creating a generator named "squares"
squares = (n**2 for n in numList)

print(next(squares))
print(next(squares))
print(next(squares))
