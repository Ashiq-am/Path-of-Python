import re


def seperateNumbersAlphabets(str):
    numbers = []
    alphabets = []
    res = re.split('(\d+)', str)

    for i in res:
        if i >= '0' and i <= '9':
            numbers.append(i)
        else:
            alphabets.append(i)

    print(*numbers)
    print(*alphabets)


str = "geeks456for53geeks"
seperateNumbersAlphabets(str)
