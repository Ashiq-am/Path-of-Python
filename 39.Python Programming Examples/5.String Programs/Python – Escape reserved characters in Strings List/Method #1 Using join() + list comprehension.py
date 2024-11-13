# Python3 code to demonstrate working of
# Escape reserved characters in Strings List
# Using list comprehension + join()

# initializing list
test_list = ["Gf-g", "is*", "be)s(t"]

# printing string
print("The original list : " + str(test_list))

# the reserved string
reserved_str = """? & | ! { } [ ] ( ) ^ ~ * : \ " ' + -"""

# the mapped escaped values
esc_dict = { chr : f"\\{chr}" for chr in reserved_str}

# performing transformation using join and list comprehension
res = [ ''.join(esc_dict.get(chr, chr) for chr in sub) for sub in test_list]

# printing results
print("The resultant escaped String : " + str(res))
