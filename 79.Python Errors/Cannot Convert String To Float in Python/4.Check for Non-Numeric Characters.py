input_string = "123.45abc"
numeric_part = ''.join(char for char in input_string if char.isdigit() or char == '.')
result = float(numeric_part)

print(result)
