import re


def has_consecutive(s, m):
    # Create target strings with m consecutive '1's and '0's
    target_1 = '1' * m
    target_0 = '0' * m

    # Check if either target string is a substring of s
    if re.search(target_1, s) or re.search(target_0, s):
        return True

    return False


s = "1001010"
m = 3
print(has_consecutive(s, m))
