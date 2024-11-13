# Python3 code for the approach

# Function to print the Kth greatest character
def printCharacter(string, L, R, K):


# Extract the substring from [L, R]
substr = string[L - 1:R]
# Sort the substring in non-increasing order
substr = sorted(substr, reverse=True)

# Return the Kth character
return substr[K - 1]


# Function to update the Jth character of the string
def updateString(string, J, C):


# Update the Jth character
string = string[:J - 1] + C + string[J:]

# Driver Code
if __name__ == '__main__':
# Given string
string = "abcddef"
# Count of queries
Q = 3

# Queries
print(printCharacter(string, 1, 2, 2))
updateString(string, 4, 'g')
print(printCharacter(string, 1, 5, 4))
