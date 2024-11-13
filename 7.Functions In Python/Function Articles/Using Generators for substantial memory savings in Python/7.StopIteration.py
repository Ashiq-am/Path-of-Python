def stopIteration():
    num = 5
    for i in range(1, num):
        yield i


def main():
    f = stopIteration()

    # 1 is generated
    print(next(f))

    # 2 is generated
    print(next(f))

    # 3 is generated
    print(next(f))

    # 4 is generated
    print(next(f))

    # 5th element - raises
    # StopIteration Exception
    next(f)


if __name__ == "__main__":
    main()


