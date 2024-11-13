# import module
import contextvars

# declaring the variable
# to it's default value
cvar = contextvars.ContextVar("cvar",
							default = "variable")

print("value of context variable cvar: \n",
	cvar.get())

# calling set method
token = cvar.set("changed")

print("\nvalue after calling set method: \n",
	cvar.get())

# checking the type of token instance
print("\nType of object instance returned by set method: \n",
	type(token))

# calling the reset method.
cvar.reset(token)

print("\nvalue after calling reset method: \n",
	cvar.get())
