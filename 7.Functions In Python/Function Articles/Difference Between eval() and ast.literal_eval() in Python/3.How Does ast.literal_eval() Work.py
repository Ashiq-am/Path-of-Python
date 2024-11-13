import ast

# Safe string evaluation
safe_expression = '{"name": "Aditya", "age": 24}'
result = ast.literal_eval(safe_expression)
print(result)

# Unsafe expression (raises ValueError)
unsafe_expression = "os.system('rm -rf /')"

 # Raises a ValueError
result = ast.literal_eval(unsafe_expression)
