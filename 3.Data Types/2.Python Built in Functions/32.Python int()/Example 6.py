class Number:
    value = 7

    def __index__(self):
        return self.value


data = Number()
print("number =", int(data))
