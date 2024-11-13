import random

def get_neighbor(x, step_size=0.1):
    neighbor = x[:]
    index = random.randint(0, len(x) - 1)
    neighbor[index] += random.uniform(-step_size, step_size)
    return neighbor
