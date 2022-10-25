from __future__ import annotations
from typing import List


class Node(object):
    metadata: list[int] = []
    children: list[Node] = []

    def __init__(self, children: List[Node], metadata: List[int]) -> None:
        self.children = children
        self.metadata = metadata

    def sum_metadata(self):
        return sum(self.metadata) + sum([child.sum_metadata() for child in self.children])

    def get_value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        value = 0
        for child_index in self.metadata:
            value += self.children[child_index-1].get_value() if child_index-1 < len(self.children) else 0

        return value



