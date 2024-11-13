a = 2.202
b = -2.202

# This inverts the sign
# for both integer as
# well as float type
c = -a
print("Minus operator value 1:", c)
c = -b
print("Minus operator value 2:", c)

# This does not inverts the sign
# for both integer as well
# as float type
c = +a
print("Plus operator value 1:", c)
c = +b
print("Plus operator value 2:", c)

a = 2
b = -2

# This inverts the sign only
# for integer type as perform
# operation as per this '-(x + 1)'.
c = ~a # -(2 + 1)
print("Invert operator value 1:", c)
c = ~b	 # -(-2 + 1)
print("Invert operator value 2:", c)
