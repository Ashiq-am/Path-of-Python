def file_func():
    f = open('sample.txt')
    return f


def main():
    f = file_func()
    print(next(f))
    print(next(f))


if __name__ == "__main__":
    main()
