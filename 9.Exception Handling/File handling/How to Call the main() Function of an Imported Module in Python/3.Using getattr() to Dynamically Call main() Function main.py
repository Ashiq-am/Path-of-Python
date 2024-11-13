# main_script.py
module_name = "example_module"
main_function_name = "main"

# Import the module dynamically
example_module = __import__(module_name)

# Dynamically call the main() function
getattr(example_module, main_function_name)()
