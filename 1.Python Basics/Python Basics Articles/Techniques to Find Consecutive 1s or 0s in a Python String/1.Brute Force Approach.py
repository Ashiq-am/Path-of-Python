def has_consecutive(s, m):
    # Initialize counters for consecutive 1s and 0s
    count_1 = count_0 = 0

    #  Loop through each character in the string
    for char in s:
        #  Update counters
        if char == '1':
            count_1 += 1
            count_0 = 0
        elif char == '0':
            count_0 += 1
            count_1 = 0

        # Check if any counter has reached m
        if count_1 >= m or count_0 >= m:
            return True

    return False


s = "11110000111111"
m = 4
print(has_consecutive(s, m))
