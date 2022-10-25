import os
import unittest

from solution import sum_metadata


class SumMetadataTestCase(unittest.TestCase):
    def test_handle_negative_in_metadata(self):
        self.assertEqual(
            0,
            sum_metadata([2, 2, 0, 2, 1, 1, 0, 2, 1, -1, -1, -1])
        )

    def test_edge_cases(self):
        self.assertEqual(
            0,
            sum_metadata([0, 0])
        )

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            sum_metadata([])

    def test_happy_path(self):
        # Problem statement's given test case
        self.assertEqual(
            138,
            sum_metadata([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
        )

    def test_only_one_tree_level(self):
        self.assertEqual(
            10,
            sum_metadata([0, 4, 1, 2, 3, 4])
        )

    def test_advent_of_code_part1(self):
        with open(os.path.join(os.path.dirname(__file__), 'testcase.txt')) as test_case_file:
            entries_raw = test_case_file.read()
            self.assertEqual(
                41760,
                sum_metadata(list(map(int, entries_raw.split())))
            )


if __name__ == '__main__':
    unittest.main()
