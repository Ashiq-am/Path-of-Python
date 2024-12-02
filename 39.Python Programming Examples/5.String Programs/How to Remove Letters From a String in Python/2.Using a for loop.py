s = "hello world"

# Initialize an empty string to store modified version of 's'
s1 = ""

# Iterate over each character in string 's'
for c in s:

    # Check if current character is not 'o'
    if c != "o":
        # If it's not 'o', append character to 's1'
        s1 += c

print(s1)