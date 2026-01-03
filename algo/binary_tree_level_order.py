"""
Binary Tree Level Order Traversal - Full Problem
Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
What is Level Order Traversal?
Level order means visiting all nodes at depth 0, then all nodes at depth 1, then depth 2, and so on. At each level, you visit nodes from left to right.
Visual Example
        3
       / \
      9   20
         /  \
        15   7
Level 0: [3]
Level 1: [9, 20]
Level 2: [15, 7]
Output: [[3], [9, 20], [15, 7]]
More Examples
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3], [9,20], [15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Example 4:
        1
       / \\
      2   3
     / \\   \
    4   5   6

Output: [[1], [2,3], [4,5,6]]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    """
    Given the root of a binary tree, return the level order traversal
    of its nodes' values (i.e., from left to right, level by level).

    Args:
        root: TreeNode - root of the binary tree

    Returns:
        List[List[int]] - level order traversal
    """
    # TODO: Implement your solution here
    if root is None:
        return []

    visited = set()
    visited.add(root)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Helper function to build a tree from a list (for testing)
def build_tree(values):
    """Builds a binary tree from a list representation."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Test cases
if __name__ == "__main__":
    # Test case 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1:", levelOrder(root1))
    # Expected: [[3], [9, 20], [15, 7]]

    # Test case 2
    root2 = build_tree([1])
    print("Test 2:", levelOrder(root2))
    # Expected: [[1]]

    # Test case 3
    root3 = build_tree([])
    print("Test 3:", levelOrder(root3))
    # Expected: []

    # Test case 4
    root4 = build_tree([1, 2, 3, 4, 5, None, 6])
    print("Test 4:", levelOrder(root4))
    # Expected: [[1], [2, 3], [4, 5, 6]]
