class GFG:

    def __init__(self, item):
        self.item = item

    def __len__(self):
        return 1


obj = GFG("Geeksforgeeks")
print(obj.__len__())
