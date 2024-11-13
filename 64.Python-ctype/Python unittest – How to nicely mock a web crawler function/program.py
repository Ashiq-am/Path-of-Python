# importing mock from unittest.mock module
from unittest.mock import Mock

# defining instance of our mock
our_mock = Mock()

# defining mock object’s __str__ method
our_mock.__str__ = Mock(return_value='GeeksforGeeks Mocking Example')

# executing str function for output
print(str(our_mock))
