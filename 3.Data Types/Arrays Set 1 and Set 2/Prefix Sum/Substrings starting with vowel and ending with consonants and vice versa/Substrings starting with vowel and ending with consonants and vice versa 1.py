'''package whatever #do not write package name here '''


# function to check if a character is vowel or not
def isVowel(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        return 1;
    return 0;


def countSpecial(str):
    cnt = 0;
    n = len(str);

    # in case of single character or empty string
    # we can't fulfill the given condition , hence the
    # count is 0.
    if (n == 1 or n == 0):
        return 0;

    # variables to store count of total vowels and
    # consonants in the string
    vow = 0
    cons = 0;

    for i in range(n):
        ch = str[i];
        vow += isVowel(ch);

    cons = n - vow;

    for i in range(n):
        ch = str[i];
        # as we encounter a vowel, we add no. of
        # consonants after it to our answer
        # and decrease the value of vow by 1,
        # indicating that now the remaining
        # string has one vowel less than current string
        if (isVowel(ch) == 1):
            vow -= 1;
            cnt += cons;

        # same case as above for consonants
        else:
            cons -= 1;
            cnt += vow;

    # finally we return the cnt as our answer
    return cnt;


# Driver code
if __name__ == '__main__':
    str = "adceba";
    count = countSpecial(str);
    print(count);

# This code is contributed by Rajput-Ji
