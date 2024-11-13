from unittest.mock import MagicMock
m = MagicMock(return_value = 10)
print(m(1, 2, debug = True), "\n")

m.assert_called_with(1, 2, debug = True)
m.assert_called_with(1, 2)
