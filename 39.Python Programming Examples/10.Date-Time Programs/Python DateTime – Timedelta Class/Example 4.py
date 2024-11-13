from datetime import timedelta

# creating the timedelat object
t1 = timedelta(days=1)
print("Original timedelta:", t1)

# multiplication
t2 = t1*5.5
print("After Multiplication:", t2)

# Subtraction
res = t2 - t1
print("After Subtraction:", res)

# addition
res += t2
print("After Addition:", res)

# division
res = t2/2.5
print("After division:", res)

# floor division
res = t2 //2
print("After floor division:", res)

# Modulo
res = t2%timedelta(days=3)
print("After Modulo:", res)
