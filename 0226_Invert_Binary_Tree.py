"""
Problem: Invert Binary Tree
LeetCode: 226
Difficulty: Easy

Topic:
- Binary Tree
- Depth-First Search
- Recursion

Approach:
- Recursively visit every node in the tree.
- Swap the left and right children of each node.
- Continue recursively for the swapped subtrees.
- Return the root of the inverted tree.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root