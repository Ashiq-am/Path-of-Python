try:
    n = int(input("Enter the number of elements: "))
    elements = []
    for _ in range(n):
        try:
            elements.append(input("Enter an element: "))
        except EOFError:
            print("Incomplete input; using default value 'None'.")
            elements.append(None)
    print(elements)
except EOFError:
    print("No input provided for number of elements.")
