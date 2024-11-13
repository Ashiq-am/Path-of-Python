import secrets

token1 = secrets.token_bytes()
token2 = secrets.token_bytes(10)

print(token1)
print(token2)
