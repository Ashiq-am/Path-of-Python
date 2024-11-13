def arithmetic_sequence(a1, d, n):
    return [a1 + (i * d) for i in range(n)]

def arithmetic_sum(a1, d, n):
    return (n / 2) * (2 * a1 + (n - 1) * d)

# Example usage
a1 = 2
d = 3
n = 10
sequence = arithmetic_sequence(a1, d, n)
sequence_sum = arithmetic_sum(a1, d, n)
print("Arithmetic Sequence:", sequence)
print("Sum of Arithmetic Sequence:", sequence_sum)
