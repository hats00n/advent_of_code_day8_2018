import os
import unittest

from solution import extract_tree


class TreeExtractTestCase(unittest.TestCase):
    def test_negative_number_in_child_node(self):
        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1, 3, -1, 2, 1, 2, 4, 5, 6])

    def test_negative_number_in_metadata(self):
        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1, 3, 0, -2, 4, 5, 6])

    def test_not_enough_numbers_in_root(self):
        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1])

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1, 0])

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([0, 1])

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1])

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([0])

    def test_not_enough_numbers_in_middle_nodes(self):
        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([1, 1, 0, 9, 1])

        with self.assertRaisesRegex(ValueError, "Corrupted File*"):
            extract_tree([2, 1, 0, 1, 0, 1, 10, 9])

    def test_happy_path(self):
        # Problem statement's given test case
        root_node = extract_tree([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
        self.assertEqual(2, len(root_node.children))
        self.assertEqual(3, len(root_node.metadata))
        self.assertEqual([1, 1, 2], root_node.metadata)


if __name__ == '__main__':
    unittest.main()
