import textwrap

s = 'hello\n\n \nworld'
s1 = textwrap.indent(text=s, prefix=' ')

print (s1)
print ("\n")

s2 = textwrap.indent(text=s, prefix='+ ', predicate=lambda line: True)
print (s2)
