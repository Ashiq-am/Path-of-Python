# define a function
def test_sum_numbers():
    assert sum([100, 200, 300, 400]) == 1000, "Result should be 1000"


# define a function
def test_sum_tuple_values():
    assert sum((100, 200, 200, 400)) == 1000, "Result should be 1000"


# Driver code
if __name__ == "__main__":
    test_sum_numbers()
    test_sum_tuple_values()

    print("Checking whether all tests are passed or not")
