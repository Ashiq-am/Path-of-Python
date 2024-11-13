# To demonstrate the use of formatters
# with positional key arguments.

# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
									"Geeks"))

# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
									"Geeks"))


print("Every {} should know the use of {} {} programming and {}"
	.format("programmer", "Open", "Source", "Operating Systems"))


# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
		.format("programmer", "Open", "Source", "Operating Systems"))


# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
.format("computer", "geeks", gfg ="GeeksforGeeks"))
