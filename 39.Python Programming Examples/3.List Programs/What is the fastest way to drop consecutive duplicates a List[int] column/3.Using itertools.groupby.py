from itertools import groupby

def drop_consecutive_duplicates(input_list):
    return [key for key, group in groupby(input_list)]

# Example usage
input_list = [1, 1, 2, 2, 3, 1, 1]
print(drop_consecutive_duplicates(input_list))  # Output: [1, 2, 3, 1]
