import random


def biased_coin_flip(bias):
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Check if the random number falls within the bias threshold for heads
    if random_number < bias:
        return "Heads"
    else:
        return "Tails"


def simulate_flips(number_of_flip, bias):
    # A dictionary with counts of 'Heads' and 'Tails'.
    result = {
        "Heads": 0,
        "Tails": 0
    }

    for _ in range(number_of_flip):
        flip_bias_res = biased_coin_flip(bias)
        result[flip_bias_res] += 1

    return result


if __name__ == "__main__":
    number_of_flips = 200
    bias = 0.60  # 60% chance of heads

    flip_results = simulate_flips(number_of_flips, bias)

    print(f"Results of {number_of_flips} biased coin flips with {bias:.2f} bias:")
    print(f"Heads: {flip_results['Heads']}")
    print(f"Tails: {flip_results['Tails']}")
