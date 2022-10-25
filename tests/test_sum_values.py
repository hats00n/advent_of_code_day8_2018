import os
import unittest

from solution import get_value


class GetValueTestCase(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(
            0,
            get_value([0, 0])
        )

    def test_happy_path(self):
        # Problem statement's given test case
        self.assertEqual(
            66,
            get_value([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
        )

    def test_advent_of_code_part2(self):
        with open(os.path.join(os.path.dirname(__file__), 'testcase.txt')) as test_case_file:
            entries_raw = test_case_file.read()
            self.assertEqual(
                25737,
                get_value(list(map(int, entries_raw.split())))
            )


if __name__ == '__main__':
    unittest.main()
