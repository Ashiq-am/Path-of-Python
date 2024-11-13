signed_integer = -1

# Adding 1<<32 to convert signed to
# unsigned integer
unsigned_integer = signed_integer+(1 << 32)
print(unsigned_integer)
