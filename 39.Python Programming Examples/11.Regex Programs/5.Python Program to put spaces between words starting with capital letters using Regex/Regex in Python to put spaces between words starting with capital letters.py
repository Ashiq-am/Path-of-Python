import re


def putSpace(input):
    # regex [A-Z][a-z]* means any string starting
    # with capital character followed by many
    # lowercase letters
    words = re.findall('[A-Z][a-z]*', input)

    # Change first letter of each word into lower
    # case
    result = []
    for word in words:
        word = chr(ord(word[0]) + 32) + word[1:]
        result.append(word)
    print(' '.join(result))


# Driver program
if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)
