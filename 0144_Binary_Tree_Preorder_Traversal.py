"""
Problem: Binary Tree Preorder Traversal
LeetCode: 144
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion
- Preorder Traversal

Approach:
- Visit the current node first.
- Recursively traverse the left subtree.
- Recursively traverse the right subtree.
- Return the values in Root -> Left -> Right order.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        if root is None:
            return []

        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right