from collections import Counter


def can_rearrange_alternately(s):
    # Count the occurrences of each character in the string
    counter = Counter(s)

    # Retrieve the counts of '0's and '1's
    count_0 = counter.get('0', 0)
    count_1 = counter.get('1', 0)

    return abs(count_0 - count_1) <= 1


s = "111001"
print(can_rearrange_alternately(s))
