def checkHarshad(n):
    # Converting integer to string
    st = str(n)
    sum = 0
    length = len(st)

    for i in st:
        sum = sum + int(i)

    # Comparing number and sum
    if (n % sum == 0):
        return "Yes"
    else:
        return "No"

number = 18
print(checkHarshad(number))

number = 15
print(checkHarshad(number))
