# Python code to split a string
# using rsplit.

# Splits at space
word = 'geeks for geeks'
print(word.rsplit())

# Splits at 'g'. Note that we have
# provided maximum limit as 1. So
# from right, one splitting happens
# and we get "eeks" and "geeks, for, "
word = 'geeks, for, geeks'
print(word.rsplit('g', 1))

# Splitting at '@' with maximum splitting
# as 1
word = 'geeks@for@geeks'
print(word.rsplit('@', 1))
