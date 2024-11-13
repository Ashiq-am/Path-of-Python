def geometric_sequence(a1, r, n):
    return [a1 * (r ** i) for i in range(n)]

def geometric_sum(a1, r, n):
    if r == 1:
        return a1 * n
    return a1 * (1 - r ** n) / (1 - r)

# Example usage
a1 = 2
r = 3
n = 5
sequence = geometric_sequence(a1, r, n)
sequence_sum = geometric_sum(a1, r, n)
print("Geometric Sequence:", sequence)
print("Sum of Geometric Sequence:", sequence_sum)
