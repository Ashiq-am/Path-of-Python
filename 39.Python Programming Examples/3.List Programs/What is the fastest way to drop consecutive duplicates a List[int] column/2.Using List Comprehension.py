def drop_consecutive_duplicates(input_list):
    return [input_list[i] for i in range(len(input_list)) if i == 0 or input_list[i] != input_list[i - 1]]

# Example usage
input_list = [1, 1, 2, 2, 3, 1, 1]
print(drop_consecutive_duplicates(input_list))  # Output: [1, 2, 3, 1]
