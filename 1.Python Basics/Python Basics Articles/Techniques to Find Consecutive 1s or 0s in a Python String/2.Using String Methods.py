def has_consecutive(s, m):
    # Create target strings with m consecutive '1's and '0's
    target_1 = '1' * m
    target_0 = '0' * m

    # Check if either target string is a substring of s
    return target_1 in s or target_0 in s


s = "11110001"
m = 4
print(has_consecutive(s, m))
