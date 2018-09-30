# Try running Doctests with `python -m doctest jumping_on_clouds.py -v`

"""
Notes: 

This one was a little difficult with the while loop 
remaining in the list boundries. Need to retry this
one pretty soon

Examples:
    >>> jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    4

    >>> jumping_on_clouds([0, 0, 0, 1, 0, 0])
    3
"""

def jumping_on_clouds(c):
    steps, cumulus, idx = 0, 0, 0
    
    while idx < len(c) - 1:
        if idx + 2 < len(c) and c[idx + 2] == cumulus:
            idx += 2
            steps += 1
        else:
            idx += 1
            steps += 1
            
    return steps


# Nose Tests
from nose.tools import assert_equal


class TestJumpingOnClouds(object):

    input_expected = [
        ([0, 0, 1, 0, 0, 1, 0], 4),
        ([0, 0, 0, 1, 0, 0], 3),
    ]

    def test_input(self):
        for in_out in self.input_expected:
            assert_equal(jumping_on_clouds(in_out[0]), in_out[1])
        print('Success')

def main():
    test = TestJumpingOnClouds()
    test.test_input()


if __name__ == '__main__':
    main()