import random

sampleList = [100, 200, 300, 400, 500]
randomList = random.choices(
sampleList, cum_weights=(5, 15, 35, 65, 100), k=5)

print(randomList)
