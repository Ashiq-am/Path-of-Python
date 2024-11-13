def Converter(str):
    result = ""
    a = str.split(" ")

    for q in a:
        if q == 'J' or 'C' or 'M':
            result += q[1:2].upper()

    return result
