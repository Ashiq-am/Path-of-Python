# test_reversal2.py

import pytest

def reverse_text(text):
    if not isinstance(text, str):
        raise ValueError('Expected a string')
    return text[::-1]

def test_reverse_text_non_string():
    with pytest.raises(ValueError):
        reverse_text(1234)
