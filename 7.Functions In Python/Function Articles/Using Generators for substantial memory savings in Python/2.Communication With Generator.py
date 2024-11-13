def fibonacci():
    values = []
    while True:

        if len(values) < 2:
            values.append(1)
        else:

            # sum up the values and
            # append the result
            values.append(sum(values))

            # pop the first value in
            # the list
            values.pop(0)

        # yield the latest value to
        # the caller
        yield values[-1]
        continue


def main():
    fib = fibonacci()
    print(next(fib))  # 1
    print(next(fib))  # 1
    print(next(fib))  # 2
    print(next(fib))  # 3
    print(next(fib))  # 5


if __name__ == "__main__":
    main()
