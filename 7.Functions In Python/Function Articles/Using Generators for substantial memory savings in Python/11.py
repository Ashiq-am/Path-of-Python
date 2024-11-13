def factorial():
    num = 0
    value = None
    response = None
    while True:
        factorial = 1
        if response:
            value = int(response)
        else:
            num = num + 1
            value = num

        for i in range(1, value + 1):
            factorial = factorial * i
        response = yield factorial


def main():
    fact = factorial()
    print(next(fact))
    print(next(fact))
    print(next(fact))
    print(fact.send(5))  # send
    print(next(fact))


if __name__ == "__main__":
    main()
