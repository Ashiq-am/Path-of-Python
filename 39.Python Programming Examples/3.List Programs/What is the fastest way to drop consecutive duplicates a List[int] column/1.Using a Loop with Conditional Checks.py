def drop_consecutive_duplicates(input_list):
    if not input_list:
        return []

    result = [input_list[0]]
    for i in range(1, len(input_list)):
        if input_list[i] != input_list[i - 1]:
            result.append(input_list[i])
    return result


# Example usage
input_list = [1, 1, 2, 2, 3, 1, 1]
print(drop_consecutive_duplicates(input_list))  # Output: [1, 2, 3, 1]
