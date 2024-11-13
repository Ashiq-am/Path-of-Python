# Another Python code to demonstrate
# working of compile() with eval.
x = 50

# Note eval is used for statement
a = compile('x == 50', '', 'eval')
print(eval(a))
