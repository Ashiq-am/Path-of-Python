a = 10
i = 2

if a > 1:

    while (i * i < a):

        if a % i == 0:
            print(a, "is not prime ")
            break

        else:
            print(a, "is prime ")
        i += 1
else:
    print(a, "is not prime ")
