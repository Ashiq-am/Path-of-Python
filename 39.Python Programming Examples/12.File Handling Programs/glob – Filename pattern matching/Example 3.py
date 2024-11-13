import glob

gen = glob.iglob("*.py")
# returns class type of gen
type(gen)

for py in gen:
	print(py)
