class ObjectCounter:
    count = 0

    def __init__(self):
        ObjectCounter.count += 1

    @staticmethod
    def display_count():
        print("Number of objects created:", ObjectCounter.count)

# Example usage:
a = ObjectCounter()
b = ObjectCounter()
ObjectCounter.display_count()
