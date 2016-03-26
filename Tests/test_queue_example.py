import add_two_numbers
import multiply_two_numbers


def test_add_two_numbers():
    assert add_two_numbers.add_two_numbers(3, 3) == 6


def test_multiply_two_numbers():
    assert multiply_two_numbers.multiply_two_numbers(2, 2) == 4


def test_string():
    class Resp:
        def __init__(self):
            self.data = {'text': "'user' is a required property"}

    response = Resp()

    assert response.data['text'] == "'user' is a required property"
