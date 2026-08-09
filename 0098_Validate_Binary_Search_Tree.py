"""
Problem: Validate Binary Search Tree
LeetCode: 98
Difficulty: Medium

Topic:
- Binary Tree
- Binary Search Tree
- Depth-First Search
- Recursion

Approach:
- Recursively validate each node using a valid range of values.
- For a node:
  - All values in the left subtree must be smaller than the node.
  - All values in the right subtree must be greater than the node.
- Update the valid range when moving to each subtree.

Time Complexity: O(n)
Space Complexity: O(h)

where h is the height of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))