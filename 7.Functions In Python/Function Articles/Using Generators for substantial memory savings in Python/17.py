def gensub1():
    yield 'A'
    yield 'B'


def gensub2():
    yield '100'
    yield '200'


def main_gen():
    yield from gensub1()
    yield from gensub2()


def main():
    delg = main_gen()
    print(next(delg))
    print(next(delg))
    print(next(delg))
    print(next(delg))


if __name__ == "__main__":
    main()
