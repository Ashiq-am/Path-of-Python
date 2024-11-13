from scipy.special import logsumexp

# logsum exp of numbers from
# 1 to 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# logsum exp of numbers from
# 10 to 15
b = [10, 11, 12, 13, 14, 15]
print([logsumexp(a), logsumexp(b)])
