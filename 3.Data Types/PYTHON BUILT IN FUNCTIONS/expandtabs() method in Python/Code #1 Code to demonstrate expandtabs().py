# Python3 code to demonstrate
# working of expandtabs()

# initializing string
str = "i\tlove\tgfg"

# using expandtabs to insert spacing
print("Modified string using default spacing: ", end ="")
print(str.expandtabs())

print("\r")

# using expandtabs to insert spacing
print("Modified string using less spacing: ", end ="")
print(str.expandtabs(2))

print("\r")

# using expandtabs to insert spacing
print("Modified string using more spacing: ", end ="")
print(str.expandtabs(12))

print("\r")
