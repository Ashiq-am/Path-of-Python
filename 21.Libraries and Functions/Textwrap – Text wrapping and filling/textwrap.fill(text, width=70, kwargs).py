import textwrap

value = """This function returns the answer as STRING and not LIST."""

# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

string = wrapper.fill(text=value)

print (string)
