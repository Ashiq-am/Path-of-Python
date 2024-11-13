def printsorted(a, n, val):
    # declare a 2-D matrix
    b = [[0 for x in range(2)] for y in range(n)]

    for i in range(0, n):
        b[i][0] = abs(a[i] - val)
        b[i][1] = i

    b.sort()

    for i in range(0, n):
        print(a[b[i][1]])


a = [7, 12, 2, 4, 8, 0]
n = len(a)
val = 6
printsorted(a, n, val)
