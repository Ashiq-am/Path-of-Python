# Another Python code to demonstrate working of compile().
x = 50

# Note eval is used for single statement
a = compile('x', 'test', 'single')
exec(a)
