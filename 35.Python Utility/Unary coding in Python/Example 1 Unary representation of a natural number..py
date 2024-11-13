# Unary code encoding
N = 8
A = []

for i in range(N):
    A.append(1)

A.append(0)

B = [str(k) for k in A]

C = "".join(B)

print("Unary code for", N,
      'is', C)
