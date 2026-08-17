"""
Problem: Diameter of Binary Tree
LeetCode: 543
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Recursively calculate the height of each subtree.
- For every node, the longest path passing through that node is
  left height + right height.
- Keep track of the maximum diameter seen during the traversal.
- Return the height of each subtree to the parent.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        height(root)

        return diameter