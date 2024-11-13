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
