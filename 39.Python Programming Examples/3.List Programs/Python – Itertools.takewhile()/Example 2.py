from itertools import takewhile


# function to test the elements
def test_func(x):
    print("Testing:", x)
    return (x.isdigit())


# using takewhile with for-loop
for i in takewhile(test_func, "11234erdg456"):
    print("Output :", i)
    print()
