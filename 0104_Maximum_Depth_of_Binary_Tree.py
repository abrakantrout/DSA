"""
Problem: Maximum Depth of Binary Tree
LeetCode: 104
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Recursively calculate the depth of the left and right subtrees.
- The depth of the current node is 1 plus the greater depth of its
  two subtrees.
- An empty tree has depth 0.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)