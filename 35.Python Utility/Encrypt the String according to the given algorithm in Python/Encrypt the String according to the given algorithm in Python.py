# Create an input field
encrypt = "banana"

# Creat a dictionary to store keys
# and values
dict = {"a": "0", "e": "1",
		"i": "2", "o": "2",
		"u": "3"}

# Reverse the string
num = encrypt[::-1]

# Replace vowels using loops
for i in dict:
	num = num.replace(i, dict[i])

# f- striings which improves readability
print(f"{num}aca")
