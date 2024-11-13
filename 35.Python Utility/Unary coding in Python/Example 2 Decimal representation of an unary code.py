# Unary code decoding

code = "111111110"
count = 0

for i in code:
    if i == "1":
        count += 1

print("decoded number is :", count)
