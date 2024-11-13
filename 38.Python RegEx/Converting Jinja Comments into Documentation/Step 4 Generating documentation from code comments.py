from jinja2 import Template

# Create Jinja template object
jinja_template = Template(template)

# Render the template
output = jinja_template.render(functions=functions)

# Print the output
print(output)
