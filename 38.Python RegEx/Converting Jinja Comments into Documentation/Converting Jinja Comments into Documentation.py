import re
from jinja2 import Template

# Read the Python file
with open("sample.py", "r") as file:
	code = file.read()

# Regular expression patterns for function definitions, comments, parameters, and return values
func_pattern = r'def\s+(\w+)\s*\(([^)]*)\)\s*:\s*"""([^"]*)"""'
param_pattern = r":param\s+(\w+):\s*([^:]+)"
return_pattern = r":return:\s*([^:]+)"

functions = []

# Find all function definitions
for match in re.finditer(func_pattern, code):
	function_name, params, docstring = match.groups()

	# Extract parameters and their comments
	parameters = {}
	param_matches = re.findall(param_pattern, docstring)

	for param, comment in param_matches:
		parameters[param] = comment.strip()

	# Extract return value comment
	return_value = re.search(return_pattern, docstring)
	return_comment = return_value.group(1) if return_value else None

	functions.append(
		{
			"name": function_name,
			"docstring": docstring,
			"parameters": parameters,
			"return_value": return_comment,
		}
	)

template = """
# Documentation

{% for func in functions %}
Function Name: {{ func.name }}
Description: {{ func.docstring }}
Parameters:
{% for param, desc in func.parameters.items() %}
- {{ param }}: {{ desc }}
{% endfor %}
Return Value: {{ func.return_value }}
{% endfor %}
"""

# Create Jinja template object
jinja_template = Template(template)

# Render the template
output = jinja_template.render(functions=functions)

# Print the output
print(output)
