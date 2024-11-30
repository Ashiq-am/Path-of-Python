# Taking input from the user
s1 = input("Enter your input (e.g., 'apple banana cherry' or 'apple,banana,cherry'): ")

# 1. Default split (splits by whitespace)
sp = s1.split()
print("Default split (by whitespace):", sp)

# 2. Space-separated input
ss = s1.split(' ')
print("Split by space:", ss)

# 3. Custom delimiter input (comma-separated in this case)
sc = s1.split(',')
print("Split by comma:", sc)