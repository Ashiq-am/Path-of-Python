from string import Template

t = Template("Hello, $name")

print(t.safe_substitute(name="Python"))
print(t.safe_substitute())
