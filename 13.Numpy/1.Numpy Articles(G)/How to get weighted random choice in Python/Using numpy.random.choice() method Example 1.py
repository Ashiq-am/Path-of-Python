from numpy.random import choice

sampleList = [100, 200, 300, 400, 500]
randomNumberList = choice(
sampleList, 5, p=[0.05, 0.1, 0.15, 0.20, 0.5])

print(randomNumberList)
