class GFG:
    def __init__(self, a):
        self.a = a

    def __len__(self):
        return len(self.a)


obj = GFG("GeeksForGeeks")
print(len(obj))
