from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(nodes: List) -> TreeNode:

    if not nodes:
        return None
    root = TreeNode(val=nodes[0])
    node_queue = deque()
    node_queue.append(root)
    i = 1
    while node_queue and i < len(nodes):
        curr = node_queue.popleft()
        curr.left = TreeNode(val=nodes[i]) if nodes[i] else None
        if i + 1 >= len(nodes):
            break
        curr.right = TreeNode(val=nodes[i + 1]) if nodes[i + 1] else None
        if curr.left:
            node_queue.append(curr.left)
        if curr.right:
            node_queue.append(curr.right)
        i += 2
    return root


tree_array = [1, 3, 2, 5, None, None, 9, 6, None, None, 7]
root = create_tree(tree_array)
