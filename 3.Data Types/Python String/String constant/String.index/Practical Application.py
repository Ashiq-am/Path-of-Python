# Python code to demonstrate the application of
# index()

# initializing target strings
voltages = ["001101 AC", "0011100 DC", "0011100 AC", "001 DC"]

# initializing argument string
type = "AC"

# initializing bit-length calculator
sum_bits = 0

for i in voltages:

    ch = i

    if (ch[len(ch) - 2] != 'D'):
     """extracts the length of bits in string"""
    bit_len = ch.index(type) - 1

    # adds to total
    sum_bits = sum_bits + bit_len

print("The total bit length of AC is : ", end="")
print(sum_bits)
