# Python program to toggle character in
# a string only with same case

# Function to toggle case
def toggle(s):
    word_list = s.split()

    # traverse through each word of the string
    for word in word_list:

        if word.islower():
            print(word.upper(), end=" ")
        elif word.isupper():
            print(word.lower(), end=" ")
        else:
            print(word, end=" ")

        # driver code


s = 'Geeks for Geeks'
toggle(s)
