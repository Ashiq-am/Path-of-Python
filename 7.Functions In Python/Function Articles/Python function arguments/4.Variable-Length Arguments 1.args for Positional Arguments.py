def sum_numbers(*args):
    # Prints the arguments and returns their sum
    print(f"{args}")
    return sum(args)


print(sum_numbers(1, 2, 3, 4))