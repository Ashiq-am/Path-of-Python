def can_rearrange_alternately(s):
    # Count the number of '0's and '1's in the string
    count_0 = s.count('0')
    count_1 = s.count('1')

    #  Check if the absolute difference between the counts is at most 1
    return abs(count_0 - count_1) <= 1


s = "11100"
print(can_rearrange_alternately(s))
