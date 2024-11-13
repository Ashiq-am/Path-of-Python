class GFG:
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s = GFG()

# sum of 1 integer
print(s.sum(1))

# sum of 2 integers
print(s.sum(3, 5))

# sum of 3 integers
print(s.sum(1, 2, 3))
