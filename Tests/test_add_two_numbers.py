import pytest
import add_two_numbers


def test_add_two_numbers():
    assert  add_two_numbers.add_two_numbers(3, 2) == 5
