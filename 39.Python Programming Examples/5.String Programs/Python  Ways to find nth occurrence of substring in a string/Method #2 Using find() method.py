# Python code to demonstrate
# to find nth occurrence of substring

# Initialising values
ini_str = "abababababab"
sub_str = "ab"
occurrence = 4

# Finding nth occurrence of substring
val = -1
for i in range(0, occurrence):
    val = ini_str.find(sub_str, val + 1)

# Printing nth occurrence
print("Nth occurrence is at", val)
