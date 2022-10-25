from typing import List

from solution.extractor import extract_tree


def sum_metadata(entries: List[int]) -> int:
    root_node = extract_tree(entries)
    return root_node.sum_metadata()


def get_value(entries: List[int]) -> int:
    root_node = extract_tree(entries)
    return root_node.get_value()
