# Cleaning & Converting Text into List
def CleConvStr2List(text):
    A, B, C = ([] for i in range(3))

    # Split line into words
    A = text.split()

    # Removing special chars from word
    for i in range(len(A)):
        B.append(''.join(e for e in A[i] if e.isalnum()))

    while ('' in B):
        B.remove("")

    # Split word into chars
    for i in range(len(B)):
        C.append(list(B[i]))

    return C


# Performing Cryptophasia
def Cryptophasia(text):
    C = []
    C = CleConvStr2List(text)

    for i in range(len(C)):
        C[i].append(C[i][0])
        C[i].append('a')
        C[i].append('y')
        del C[i][0]

    D = []
    word = ''

    for i in range(len(C)):
        D.append(word.join(C[i]))

    return " ".join(D)


# Driver Code
print(Cryptophasia('Apple'))
print(Cryptophasia('GeeksforGeeks'))
print(Cryptophasia('happy'))
