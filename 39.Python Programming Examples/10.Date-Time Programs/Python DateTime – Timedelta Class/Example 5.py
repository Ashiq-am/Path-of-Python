from datetime import timedelta

# creating the timedelat object
t1 = timedelta(days=1)
print("Original timedelta:", t1)

# Negatiob of timedelta object
t1 = -(t1)
print("After Negation:", t1)

# Getting Abosulte value
t1 = abs(t1)
print("Absolute Value:", t1)

# Getting string representation
print("String representation:", str(t1))

# Getting Constructor call
print("Constructor call:", repr(t1))
