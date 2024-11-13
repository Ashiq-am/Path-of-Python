class Demo:
    def __getitem__(self, key):
        # print a[1], a[1, 2],
        # a[1, 2, 3]
        print(key)

        return key


a = Demo()

# => slice 1
a[1]

# => slice(1, 2)
a[1, 2]

# => (1, 2, 3)
a[1, 2, 3]
