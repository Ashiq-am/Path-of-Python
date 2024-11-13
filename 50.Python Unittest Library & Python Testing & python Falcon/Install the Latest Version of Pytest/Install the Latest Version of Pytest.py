import pytest


def evenMethod(num):
    return num % 2 == 0


def evenTest():
    assert evenMethod(22) == True
    with pytest.raises(AssertionError):
        assert evenMethod(7) == True


if __name__ == "__main__":
    pytest.main()
