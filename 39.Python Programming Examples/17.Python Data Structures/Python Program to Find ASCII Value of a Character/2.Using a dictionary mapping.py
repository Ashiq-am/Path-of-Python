def method2(char):
    ascii_dict = {c: ord(c) for c in char}
    return ascii_dict[char]

character = 'D'
print("ASCII value of", character, "is:", method2(character))
