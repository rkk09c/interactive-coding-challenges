"""
Challenge: Hour glass sum

Given a input of a 6x6 matrix

a0 b0 c0 d0 e0 f0
a1 b1 c1 d1 e1 f1
a2 b2 c2 d2 e2 f2
a3 b3 c3 d3 e3 f3
a4 b4 c4 d4 e4 f4
a5 b5 c5 d5 e5 f5

select all the "hourglasses"
a0 b0 c0
   b1
a2 b2 c2

...

d3 e3 f3
   e4
d5 e5 f5

create the summation of each hourglass
sum(d3, e3, f3,, e4, d5, e5, f5)

and return the largest positive integer sum

>>> input_array = [
        [1, 1, 1 0, 0, 0],
        [0, 1, 0 0, 0, 0],
        [1, 1, 1 0, 0, 0],
        [0, 0, 2 4, 4, 0],
        [0, 0, 0 2, 0, 0],
        [0, 0, 1 2, 4, 0],
    ]
>>> hour_glass_sum(input_array)
    19

"""
class HourGlassSum(object):

    def __init__(self, array, hourglass_matrix_size):
        self.matrix = array
        self.matrix_size = len(array[0])
        self.hourglass_matrix_size = hourglass_matrix_size
        self.hourglass_matrix_middle = hourglass_matrix_size // 2

    def check_bounds(self, tb_idx, lr_idx):
        left_bound = lr_idx - self.hourglass_matrix_middle >= 0
        right_bound = lr_idx + self.hourglass_matrix_middle <= self.matrix_size
        bottom_bound = tb_idx + self.hourglass_matrix_size <= self.matrix_size
        return all([left_bound, right_bound, bottom_bound])

    def row_sum(self, tb_idx, lr_idx, row_increment):
        grow = abs(row_increment - self.hourglass_matrix_middle)
        return sum(self.matrix[tb_idx + row_increment][lr_idx - grow : lr_idx + grow + 1])

    def hour_glass_sum(self):
        hourglass_max = None

        for tb_idx, top_to_bottom in enumerate(self.matrix):
            for lr_idx, left_to_right in enumerate(top_to_bottom):
                if self.check_bounds(tb_idx, lr_idx):
                    result = 0
                    for row_increment in range(self.hourglass_matrix_size):
                        result += self.row_sum(tb_idx, lr_idx, row_increment)
                    if hourglass_max is None or result > hourglass_max:
                        hourglass_max = result
        
        return hourglass_max



from nose.tools import assert_equal


class TestHourGlassSum(object):

    test_case_1 = ([
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ], 19)

    test_case_2 = ([
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ], 28)

    def test_hour_glass_sum(self):
        for test in [self.test_case_1, self.test_case_2]:
            assert_equal(HourGlassSum(test[0], 3).hour_glass_sum(), test[1])
        
        print("Success: test_hour_glass_sum")

def main():
    test = TestHourGlassSum()
    test.test_hour_glass_sum()

if __name__ == "__main__":
    main()

