import re

example = (re.search(r"(?:AB)","ACABC"))
print(example)
print(example.groups())

result = re.search(r"(\w*), (\w*)","geeks, best")
print(result.groups())
