"""
The point of this exercise it to repeat the given
string n number of times and find how many times
the letter 'a' is repeated

Examples
    >>> repeated_string('aba', 10)
    7

    >>> repeated_string('a', 1000000)
    1000000
"""

def repeated_string(string, n):
    if not string or 'a' not in string:
        return 0

    mult_factor = n//len(string)
    remainder = n%len(string)


    # Count occurrances of a in string
    string_counter, remainder_counter = 0, 0

    for idx, letter in enumerate(string):
        if letter == 'a':
            string_counter += 1
        if idx < remainder and letter == 'a':
            remainder_counter += 1

    return (string_counter * mult_factor) + remainder_counter


# Nose Tests
from nose.tools import assert_equal


class TestRepeatedString(object):

    def test_repeated_string(self):
        input = ('aba', 10)
        expected = 7
        assert_equal(repeated_string(input[0], input[1]), expected)
        print('Success: test_repeated_string')

    def test_single_char(self):
        input = ('a', 1000000)
        expected = 1000000
        assert_equal(repeated_string(input[0], input[1]), expected)
        print('Success: test_single_char')

    def test_no_a(self):
        input = ('bcb', 10)
        expected = 0
        assert_equal(repeated_string(input[0], input[1]), expected)
        print('Success: test_no_a')


def main():
    test = TestRepeatedString()
    test.test_repeated_string()
    test.test_single_char()
    test.test_no_a()


if __name__ == '__main__':
    main()