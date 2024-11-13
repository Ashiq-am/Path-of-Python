def stopIteration():
    num = 5
    for i in range(1, num):
        if i == 3:
            raise StopIteration
        yield i


def main():
    f = stopIteration()

    # 1 is generated
    print(next(f))

    # 2 is generated
    print(next(f))

    # StopIteration raises and
    # code exits
    print(next(f))
    print(next(f))


if __name__ == "__main__":
    main()
