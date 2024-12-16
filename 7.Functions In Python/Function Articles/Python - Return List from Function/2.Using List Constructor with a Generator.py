def generate_list(n):
    return list(i for i in range(n) if i % 2 == 0)

res = generate_list(10)
print(res)