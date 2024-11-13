def create_multipliers():
    return [lambda x, i=i: i * x for i in range(6)]


for multiplier in create_multipliers():
    print(multiplier(3))
