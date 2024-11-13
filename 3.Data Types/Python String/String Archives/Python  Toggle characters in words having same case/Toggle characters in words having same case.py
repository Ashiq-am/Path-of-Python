# Python program to toggle character in
# a string only with same case

# Function to toggle case
def toggle(s):
    word_list = s.split()

    # traverse through each word of the string
    for word in word_list:

        # initially assume all the characters in word
        # are in the same case and set the flag to 1
        flag = 1

        # check the case of the first
        # character in the word
        if word[0].islower():

            # if the case is lower set the r value to 1
            r = 1

            # traverse through the remaining
            # characters in the word
            for j in word:

                # if any of the characters are in upper case
                if j.isupper():
                    # then set the flag to 0
                    flag = 0
                    break

        else:
            # if the case is upper
            # set the r value to 1
            r = 0

            # traverse through the remaining
            # characters in the word
            for j in word:

                # if any of the characters are in lower case
                if j.islower():
                    # then set the flag to 0
                    flag = 0
                    break

        # if the flag is 0 then print the word as it is
        if flag == 0:
            print(word, end=" ")

        else:
            # if the word is in lower case
            # then print the word in upper case
            if r == 1:
                print(word.upper(), end=" ")

            # if the word is in upper case
            # then print the word in lower case
            else:
                print(word.lower(), end=" ")

        # driver code


s = 'Geeks for Geeks'
toggle(s)
