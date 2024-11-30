# Truncate with ellipsis
s1 = "Welcome to Python programming!"
n = 10
s2 = s1[:n] + "..." if len(s1) > n else s1
print(s2)

# output: Welcome to...