def simulate_flips(number_of_flip, bias):
    # dict: A dictionary with counts of 'Heads' and 'Tails'.

    result = {
        "Heads": 0,
        "Tails": 0
    }

    for _ in range(number_of_flip):
        flip_bias_res = biased_coin_flip(bias)
        result[flip_bias_res] += 1

    return result
