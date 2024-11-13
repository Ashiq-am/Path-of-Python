# Python3 code for the grouper recipe

# import the existing itertool izip_longest
from itertools import izip_longest


# function for the grouper recipe
def grouper(iterable, n, fillvalue='x'):
    # create 'n'-blocks for collection
    args = [iter(iterable)] * n

    # collect data into fixed length blocks of
    # length 'n' using izip_longest and store
    # result as a list
    ans = list(izip_longest(fillvalue=fillvalue, *args))

    # (optional) loop to convert ans to string
    t = len(ans)
    for i in range(t):
        ans[i] = "".join(ans[i])

    # return ans as string
    return " ".join(ans)


# Driver code
s = "ABCDEFG"
k = 3

result = grouper(s, k)
print(result)
