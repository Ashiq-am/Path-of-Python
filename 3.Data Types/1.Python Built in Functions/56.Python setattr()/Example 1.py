class Gfg:
	name = None
	descr = None


# initializing object
gfg = Gfg()

print("Before using setattr:\n"
	f"\tname: {gfg.name}\n"
	f"\tdescr: {gfg.descr}")

# setting value using setattr
setattr(gfg, "name", "GeeksForGeeks")
setattr(gfg, "descr", "CS Portal")

print("After using setattr:\n"
	f"\tname: {gfg.name}\n"
	f"\tdescr: {gfg.descr}")

# creating new attribute using setattr
setattr(gfg, 'value', 5)
print(f"\nNew attribute created, gfg.value: {gfg.value}")
