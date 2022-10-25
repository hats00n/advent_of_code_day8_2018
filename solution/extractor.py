from typing import Tuple, List
from solution.node import Node


def extract_tree(entries: List[int]) -> Node:
    """
    This function accepts the entries in the license file and calculates the sum of all metadatas
    :param entries: list of integer representing the lisence file
    :return: sum of the metadata represented by entries
    """
    root_node, exit_index = _extract_tree_at_index(entries, 0)

    # if not equal , that means there are some extra data on the file
    if exit_index != len(entries):
        raise ValueError("Corrupted File, File contains more info than header suggests")

    return root_node


def _extract_tree_at_index(entries: List[int], index: int) -> Tuple[Node, int]:
    """
    This function extracts a license node that starts from index, the approach of parsing is as described in part1
    :param entries: the entries in lisence file
    :param index: the index that this node starts from
    :return: a tuple, representing the metadata within this node (AND CHILD NODES) and the index when the node ends
    """
    if index > len(entries) - 2:
        raise ValueError("Corrupted File, Header @{} must have at least two nodes".format(index))

    child_nodes = []
    number_of_children = entries[index]
    number_of_meta_data = entries[index + 1]
    node_header_cursor = index + 2

    if number_of_children < 0:
        raise ValueError("Corrupted File, Header@{} contains negative child node count".format(index))
    if number_of_meta_data < 0:
        raise ValueError("Corrupted File, Header@{} contains negative metadata count".format(index))

    for child_index in range(number_of_children):
        extracted_node, node_header_cursor = _extract_tree_at_index(entries, node_header_cursor)
        child_nodes.append(extracted_node)

    metadata = entries[node_header_cursor:node_header_cursor + number_of_meta_data]
    return Node(child_nodes, metadata), node_header_cursor + number_of_meta_data
