originalVect = [1, 2, 3, 4]
clonedRowVect = originalVect[:]

clonedColumnVect = [[x] for x in originalVect]

print("Original Row Vector:", originalVect)
print("Cloned Row Vector:", clonedRowVect)
print("Cloned Column Vector:")

for row in clonedColumnVect:
    print(row)

