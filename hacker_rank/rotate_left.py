"""
Challenge: Rotate Array Left

given an array, rotate entries left n times

Example:
    >>> rotate_left(1, [1, 2, 3, 4, 5])
    [2, 3, 4, 5, 1]

    >>> rotate_left(3, [1, 2, 3, 4, 5])
    [4, 5, 1, 2, 3]
"""

def rotate_left(rotations, array):
    rotations = rotations % len(array)
    for _ in range(rotations):
        shift_num = array.pop(0)
        array.append(shift_num)

    return array


from nose.tools import assert_equal


class TestRotateLeft(object):

    def test_rotate(self):
        test_array = [1, 2, 3, 4, 5]
        rotations = 3
        expected_result = [4, 5, 1, 2, 3]
        assert_equal(rotate_left(rotations, test_array), expected_result)
        print('Success: test_rotate')


def main():
    test = TestRotateLeft()
    test.test_rotate()


if __name__ == "__main__":
    main()
