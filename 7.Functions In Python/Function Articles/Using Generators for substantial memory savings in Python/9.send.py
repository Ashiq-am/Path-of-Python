def factorial():
    num = 1
    while True:
        factorial = 1

        for i in range(1, num + 1):
            # determines the factorial
            factorial = factorial * i

        # produce the factorial to the caller
        response = yield factorial

        # if the response has value
        if response:

            # assigns the response to
            # num variable
            num = int(response)
        else:

            # num variable is incremented
            # by 1
            num = num + 1


def main():
    fact = factorial()
    print(next(fact))
    print(next(fact))
    print(next(fact))
    print(fact.send(5))  # send
    print(next(fact))


if __name__ == "__main__":
    main()
