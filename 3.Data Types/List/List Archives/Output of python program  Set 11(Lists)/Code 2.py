data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)
