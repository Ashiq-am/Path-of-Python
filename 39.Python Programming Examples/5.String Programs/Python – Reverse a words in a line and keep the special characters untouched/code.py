def reverStringsInLine(s):
    sl = s.split(' ')
    rsl = ''

    for word in sl:
        str_word = ''
        rev_sub_word = ''

        for ch in word:

            if ch.isalnum():
                str_word += ch

            else:

                # If it is special character, then
                # reverse non special characters and
                # append special character

                rev_sub_word += str_word[::-1] + ch

                # Clear the old stached character, as
                # it is already reversed
                str_word = ''

            # Keep appening each words, aslo add words
        # ending with non-special character
        r_word = rev_sub_word + str_word[::-1]
        rsl += r_word + ' '
    return rsl


s = 'Bangalore is@#$!123locked locked again in jul2020'

print(reverStringsInLine(s))
