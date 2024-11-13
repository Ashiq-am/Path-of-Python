# Python program to demonstrate working of rfind()
# in whole string
word = 'geeks for geeks'

# Returns highest index of the substring
result = word.rfind('geeks')
print ("Substring 'geeks' found at index :", result )

result = word.rfind('for')
print ("Substring 'for' found at index :", result )

word = 'CatBatSatMatGate'

# Returns highest index of the substring
result = word.rfind('ate')
print("Substring 'ate' found at index :", result)
