if __name__ == '__main__':
    n = 6;
    a = [3, 6, 2, 8, 9, 2];
    pf = [0 for i in range(n + 2)];
    for i in range(n):
        pf[i + 1] = pf[i] + a[i];

    q = [[2, 3], [4, 6], [1, 5], [3, 6]];
    for i in range(4):
        l = q[i][0];
        r = q[i][1];

        # Calculating sum from r to l.
        print(pf[r] - pf[l - 1]);

# This code is contributed by gauravrajput1
