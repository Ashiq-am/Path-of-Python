import random


def biased_coin_flip(bias):
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Check if the random number falls within the bias threshold for heads
    if random_number < bias:
        return "Heads"
    else:
        return "Tails"
