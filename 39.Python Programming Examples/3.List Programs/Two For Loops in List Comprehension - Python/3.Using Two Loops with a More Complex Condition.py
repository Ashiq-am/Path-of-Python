# Generating pairs with specific conditions
ans = [(a, b) for a in range(1, 6) for b in range(1, 6) if a % 2 == 0 and b % 2 != 0]

print(ans)