s = "hello"
try:
    s.index("e")
    print("Character found!")
except ValueError:
    print("Character not found!")